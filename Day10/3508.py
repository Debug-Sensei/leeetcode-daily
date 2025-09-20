from collections import deque, defaultdict
import bisect

class Router:
    def __init__(self, memoryLimit: int):
        self.limit = memoryLimit
        self.queue = deque()  # maintain global packet order
        self.seen = set()     # for duplicates
        self.dest_map = defaultdict(list)  # dest -> sorted timestamps

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source, destination, timestamp)
        if packet in self.seen:
            return False

        # Evict oldest if full
        if len(self.queue) == self.limit:
            old = self.queue.popleft()
            self.seen.remove(old)
            _, d, t = old
            idx = bisect.bisect_left(self.dest_map[d], t)
            if idx < len(self.dest_map[d]) and self.dest_map[d][idx] == t:
                self.dest_map[d].pop(idx)

        # Add new packet
        self.queue.append(packet)
        self.seen.add(packet)
        bisect.insort(self.dest_map[destination], timestamp)
        return True

    def forwardPacket(self) -> list[int]:
        if not self.queue:
            return []
        packet = self.queue.popleft()
        self.seen.remove(packet)
        _, d, t = packet
        idx = bisect.bisect_left(self.dest_map[d], t)
        if idx < len(self.dest_map[d]) and self.dest_map[d][idx] == t:
            self.dest_map[d].pop(idx)
        return list(packet)

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        times = self.dest_map[destination]
        left = bisect.bisect_left(times, startTime)
        right = bisect.bisect_right(times, endTime)
        return right - left