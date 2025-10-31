class BowlingGame:
    def __init__(self):
        self.frames=[]
        self.score_total=0

    def roll(self, pins):
        
        if 0>pins or 10<pins:
            raise Exception("Only valid roll")
        self.frames.append(pins)

        process_frames=self.process_self_frames()
        
        if len(process_frames)>10 and sum(process_frames[-2])!=10:
            raise Exception("Invalid frame")
            
        for frame in process_frames:
            if sum(frame)>10:
                raise Exception("Invalid frame")
        if len(process_frames)>10:
            if len(process_frames[9])==2 and sum(process_frames[9])==10:
                if len(process_frames[10])>1:
                    raise Exception("Invalid frame")
            

    def process_self_frames(self):
        process_frames=[]
        jump=False
        for idx,frame in enumerate(self.frames):
            if jump:
                jump=False
                continue
            if idx+1<len(self.frames):
                if frame==10:
                    process_frames.append([frame])
                    
                else:
                    process_frames.append([self.frames[idx],self.frames[idx+1]])
                    jump=True
            else:
                process_frames.append([frame])
        return process_frames
        
    def score(self):
        process_frames=self.process_self_frames()
        tiros=[item for row in process_frames for item in row]
        if process_frames==[] or len(process_frames)<10:
            raise Exception("Empty game")

        [print(idx+1,item) for idx,item in enumerate(process_frames)]
        
        ultimos=process_frames[10:]
        
        if len(ultimos)==1:
            if ultimos[0][0]==10 and (sum(process_frames[9])!=10 or process_frames[9][0]==10):
                raise Exception("Empty game")
                
        if len(ultimos)==2:
            if all([item==10 for row in ultimos for item in row]) and process_frames[9][0]!=10:
                raise Exception("Empty game")
            if process_frames[9][0]!=10:
                raise Exception("Empty game")
        if len(ultimos)==0:
            if sum(process_frames[9])==10:
                raise Exception("Empty game")
            
        
                
        for idx,frame in enumerate(process_frames):
            if idx>9:
                continue
            
            if sum(frame)==10:
                if len(frame)==1:
                    if idx+1<len(process_frames):
                        self.score_total+=sum([item for row in process_frames[idx+1:] for item in row][:2])+10
                        
                    else:
                        pass
                else:
                    if idx+1<len(process_frames):
                        self.score_total+=process_frames[idx+1][0]+10
            else:
                self.score_total+=sum(frame)
            
        return self.score_total
