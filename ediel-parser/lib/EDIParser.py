import json
from datetime import datetime
from pydifact.message import Message as PMessage
from pydifact.segments import Segment as PSegment

from lib.Segment import Segment, Group
from lib.UNSegment import UNSegment
from lib.UNMessage import UNMessage
import lib.ediTools as edi

class EDIParser():
    def __init__(self, payload: str, format: str):
        self.payload = payload
        self.format = format
        self.segments = self.parse()

    def parse(self):
        if self.format == 'edi':
            return self.parse_edi()
        elif self.format == 'json':
            return self.parse_json()

    def get_props_for(self, segment) -> (str, list):
        if self.format == 'json':
            return segment.pop(0), segment
        elif self.format == 'edi':
            return segment.tag, segment.elements

    def load_segment(self, segment):
        tag, elements = self.get_props_for(segment)
        template = UNSegment(tag)
        template.load(elements)
        return template

    def parse_edi(self):
        message = PMessage.from_str(self.payload)
        segments = Group(self.format).structure(
            *map(self.load_segment, message.segments)
        )
        return segments

    def parse_json(self):
        segments = []
        segment_list = self.flatten_json()
        segments = Group(self.format).structure(
            *map(self.load_segment, segment_list)
        )
        return segments

    def flatten_json(self) -> list:
        message = json.loads(self.payload)
        result = []
        for segment in message:
            result.append(self._flatten_json(segment))
        return result

    def _flatten_json(self, segment) -> list:
        # flatten the segments to arrays
        # load as edi message
        segments = []
        if type(segment) is dict:
            for k in segment.keys():
                cur = segment[k]
                segments.append(self._flatten_json(cur))
            return segments
        else:
            return segment

    """
    Generate aperak based on payload information
    """
    def create_aperak(self, segments = None) -> [Segment]:
        aperak = UNMessage('APERAK')
        aperak['UNH'][1][0] = 'APERAK'
        aperak['UNH'][1][1] = 'D'
        aperak['UNH'][1][2] = '96A'
        aperak['UNH'][1][3] = 'UN'
        aperak['UNH'][1][4] = 'EDIEL2'
        aperak['BGM'][3] = '27'
        aperak['DTM'][0][0] = '137'
        aperak['DTM'][0][1] = edi.format_timestamp(datetime.now())
        aperak['DTM'][0][2] = '203' # CCYYMMDDHHmm

        reference_no = self.segments['BGM']
        print(reference_no)



        print(aperak)

    """
    Dictionary out of payload segments
    """
    def toDict(self, segments = None) -> list:
        segments = self.segments if segments is None else segments
        raw_result = map(lambda s: s.toDict(), self.segments)
        result = filter(lambda s: s is not None, raw_result)
        return list(result)

    """
    List out of payload segments
    """
    def toList(self, segments = None) -> list:
        segments = self.segments if segments is None else segments
        raw_result = map(lambda s: [s.tag, s.toList()], self.segments)
        result = filter(lambda s: s is not None, raw_result)
        return list(result)

    """
    EDI string out of payload segments
    """
    def toEdi(self, segments = None) -> str:
        segments = self.segments if segments is None else segments
        message = PMessage()
        for s in self.segments:
            elements = s.toList()
            if elements is not None and len(elements) > 0:
                tag = s.tag
                segment = PSegment(tag, *elements)
                message.add_segment(segment)
        return message.serialize()

