from typing import List
import heapq


class NumMeetingRooms:
    def __init__(self, meetings: List[List[int]]):
        self.meetings: List[List[int]] = meetings
        self.num_meetings: int = len(self.meetings)

    def get_num_meeting_rooms(self) -> int:
        self.meetings.sort(key=lambda x: x[0])
        end_times: List[int] = []

        for meeting in self.meetings:
            if len(end_times) == 0:
                end_times.append(meeting[1])
                heapq.heapify(end_times)
            else:
                earliest_end_time: int = end_times[0]
                if meeting[0] >= earliest_end_time:
                    end_times.pop(0)
                end_times.append(meeting[1])
                heapq.heapify(end_times)

        return len(end_times)


num_meeting_rooms = NumMeetingRooms([[0, 30], [5, 10], [15, 20]])
print(num_meeting_rooms.get_num_meeting_rooms())
