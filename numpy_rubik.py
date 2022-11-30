import numpy as np






class np_cube:
    
    def __init__(self):
        # this is a change to test git cli dafsfa
        self.cube_size=3
        self.color_key={
                        'front':(1 ,'green'),
                        'back':(2 ,'yellow'),
                        'top':(3 ,'white'),
                        'bottom':(4 ,'blue'),
                        'left':(5 ,'orange'),
                        'right':(6 ,'red'),
                        }
                        
        self.face_coor={
                        'front':[(0,y,x) for y in range(1,self.cube_size+1) for x in range(1,self.cube_size+1)],
                        'back':[(self.cube_size+1,y,x) for y in range(1,self.cube_size+1) for x in range(1,self.cube_size+1)],
                        'top':[(z,0,x) for z in range(1,self.cube_size+1) for x in range(1,self.cube_size+1)],
                        'bottom':[(z,self.cube_size+1,x) for z in range(1,self.cube_size+1) for x in range(1,self.cube_size+1)],
                        'left':[(z,y,0) for z in range(1,self.cube_size+1) for y in range(1,self.cube_size+1)],
                        'right':[(z,y,self.cube_size+1) for z in range(1,self.cube_size+1) for y in range(1,self.cube_size+1)],
                       }  
                        
                        
                        
        self.cube=self.create_cube()
        
        
        
        
        
    def create_cube(self):
        shpe=[self.cube_size+2 for i in range(3)]
        cube=np.zeros(shpe)
        
        
        for face in self.face_coor:
            fcoor=self.face_coor[face]
            for z,y,x in fcoor:
                cube[z][y][x]=self.color_key[face][0]
                
        return cube
        
        
        
    def rotate_face(self,face,direction):
        # (1,0) rot cube forward
        # (0,1) rot cube backward
        # (1,-1) rot top of cube left
        # (-1,1) rot top of cube right
        # (0,-1) rot front of cube left
        # (-1,0) rot front of cube right
        
        right=(1,0)
        left=(0,1)
        dire=None
        
        cube=self.cube
        
        
        
        if direction=='right':
            dire=right
        elif direction=='left':
            dire=left
        
        
        
        
        if face=='front':
            self.cube[0]=np.rot90(self.cube[0],1,dire)
            
            
        elif face=='back':
            
            cube=np.rot90(cube,2,(1,0)) #rotate cube forward twice
            
            for i in range(2):
                cube[i]=np.rot90(cube[i],1,dire)
                
            cube=np.rot90(cube,2,(1,0)) #rotate back
            self.cube=cube
            
            
        elif face=='top':
            
            cube=np.rot90(cube,1,(1,0))
            
            for i in range(2):
                cube[i]=np.rot90(cube[i],1,dire)
                
            cube=np.rot90(cube,1,(0,1))
            self.cube=cube
            
            
        elif face=='bottom':
            
            cube=np.rot90(cube,1,(0,1))
            
            for i in range(2):
                cube[i]=np.rot90(cube[i],1,dire)
                
            cube=np.rot90(cube,1,(1,0))
            self.cube=cube
            
            
        elif face=='left':
            
            cube=np.rot90(cube,1,(-1,0))
            
            for i in range(2):
                cube[i]=np.rot90(cube[i],1,dire)
                
            cube=np.rot90(cube,1,(0,-1))
            self.cube=cube
            
            
        elif face=='right':
            cube=np.rot90(cube,1,(0,-1))
            
            for i in range(2):
                cube[i]=np.rot90(cube[i],1,dire)
                
            cube=np.rot90(cube,1,(-1,0))
            self.cube=cube
        
            
        print(cube)
            
            
            
            
                
                
        
            
            
                   
                   
        
        
        
        
        
        # cube=np.rot90(cube,1,(1,0)) #flips forward
        
        
        
        
        
        
        
        
        
        

if __name__ == '__main__':
    
    np_cube()
    
    