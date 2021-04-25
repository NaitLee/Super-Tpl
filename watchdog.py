import os, sys, time, datetime, converter

class Watchdog():
    def __init__(self, path_of_files):
        self.path_of_files = path_of_files
        fileset = set()
        for i, j, k in os.walk(path_of_files):
            for l in k:
                newpath = os.path.join(i, l)
                fileset.add(newpath)
        self.files = list(fileset)
        self.oldstats = {}
        for i in self.files:
            self.oldstats[i] = os.stat(i).st_mtime
    def watch(self):
        newstats = {}
        for i in self.files:
            newstats[i] = os.stat(i).st_mtime
        for i in newstats:
            if newstats[i] != self.oldstats[i]:
                self.bark()
                break
        self.oldstats = newstats
    def bark(self):
        current_time = datetime.datetime.now()
        print(f'[{current_time}] Woof~ Building template...', end=' \t', flush=True)
        converter.convert(self.path_of_files)
        print('Done!')

if __name__ == '__main__':
    watchdog = Watchdog(sys.argv[1])
    try:
        while True:
            time.sleep(1.0)
            watchdog.watch()
    except KeyboardInterrupt:
        pass
