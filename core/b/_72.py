
import time

class _72:
    def __init__(self):
        self.cmds = {}
    def _73(self, uid):
        now = time.time()
        if uid not in self.cmds:
            self.cmds[uid] = []
        self.cmds[uid] = [t for t in self.cmds[uid] if now - t < 60]
        if len(self.cmds[uid]) >= 10:
            return True
        self.cmds[uid].append(now)
        return False
