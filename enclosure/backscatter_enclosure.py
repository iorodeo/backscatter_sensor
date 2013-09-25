from __future__ import print_function
import math
from py2scad import *


class BackScatterEnclosure(object):

    def __init__(self,param): 
        self.param = param
        self.makeLayer0()
        self.makeLayer1()
        self.makeMask()
        self.makeTop()
        self.makeJigPlate()
        self.makeJigMount()

    def makeLayer0(self):
        holeList = []
        diskDiam = self.param['disk diameter']
        holeAngle = self.param['join hole angle']
        holeInset = self.param['join hole inset'] 
        holePosRadius = 0.5*diskDiam - holeInset
        holeDiam = self.param['4-40 tap']
        thickness = self.param['layer0 thickness']
        holeAngleOffset = 0.5*holeAngle
        for i in range(int(2.0*math.pi/holeAngle)):
            x = holePosRadius*math.cos(holeAngle*i + holeAngleOffset)
            y = holePosRadius*math.sin(holeAngle*i + holeAngleOffset)
            holeList.append((x,y,holeDiam))
        self.layer0 = disk_w_holes(thickness,diskDiam,holes=holeList)

    def makeLayer1(self):
        holeList = []
        diskDiam = self.param['disk diameter']
        holeAngle = self.param['join hole angle']
        holeInset = self.param['join hole inset'] 
        holePosRadius = 0.5*diskDiam - holeInset
        holeDiam = self.param['4-40 clr']
        thickness = self.param['layer1 thickness']
        # Add join holes
        holeAngleOffset = 0.5*holeAngle
        for i in range(int(2.0*math.pi/holeAngle)):
            x = holePosRadius*math.cos(holeAngle*i + holeAngleOffset)
            y = holePosRadius*math.sin(holeAngle*i + holeAngleOffset)
            holeList.append((x,y,holeDiam))
        # Add pcb mount holes
        pcbHoleX, pcbHoleY = self.param['pcb hole spacing']
        pcbHoleDiam = self.param['4-40 tap']
        for i in (-1,1):
            for j in (-1,1):
                x = i*0.5*pcbHoleX
                y = j*0.5*pcbHoleY
                holeList.append((x,y,pcbHoleDiam))
        self.layer1 = disk_w_holes(thickness,diskDiam,holes=holeList)
        # Add pcb cutout
        cutX,cutY = self.param['pcb cutout size']
        cutCubeSize = (cutX,cutY,2*thickness)
        cutCube = Cube(cutCubeSize)
        self.layer1 = Difference([self.layer1,cutCube])

    def makeMask(self):
        diskDiam = self.param['disk diameter']
        diskThickness = self.param['mask thickness']
        screwX, screwY = self.param['mask screw spacing']
        screwDiam = self.param['mask screw diameter']
        holeList = []
        for i in (-1,1):
            for j in (-1,1):
                x = i*0.5*screwX
                y = j*0.5*screwY
                holeList.append((x,y,screwDiam))

        holeAngle = self.param['join hole angle']
        holeInset = self.param['join hole inset'] 
        holePosRadius = 0.5*diskDiam - holeInset
        holeDiam = self.param['4-40 clr']
        holeAngleOffset = 0.5*holeAngle
        for i in range(int(2.0*math.pi/holeAngle)):
            x = holePosRadius*math.cos(holeAngle*i + holeAngleOffset)
            y = holePosRadius*math.sin(holeAngle*i + holeAngleOffset)
            holeList.append((x,y,holeDiam))

        self.mask = disk_w_holes(diskThickness, diskDiam, holes=holeList)

        for hole in self.param['mask rectangular holes'].values():
            w, h = hole['size']
            x, y = hole['pos']
            cutCube = Cube(size=(w,h,2*diskThickness))
            cutCube = Translate(cutCube,v=(x,y,0))
            self.mask = Difference([self.mask, cutCube])

    def makeTop(self):
        holeList = []
        diskDiam = self.param['disk diameter']
        holeAngle = self.param['join hole angle']
        holeInset = self.param['join hole inset'] 
        holePosRadius = 0.5*diskDiam - holeInset
        holeDiam = self.param['4-40 clr']
        thickness = self.param['top thickness']
        holeAngleOffset = 0.5*holeAngle
        for i in range(int(2.0*math.pi/holeAngle)):
            x = holePosRadius*math.cos(holeAngle*i + holeAngleOffset)
            y = holePosRadius*math.sin(holeAngle*i + holeAngleOffset)
            holeList.append((x,y,holeDiam))
        self.top = disk_w_holes(thickness,diskDiam,holes=holeList)


    def makeJigPlate(self):
        plateX, plateY = self.param['jig plate size']
        plateThickness = self.param['jig plate thickness']
        diskDiam = self.param['disk diameter']
        holeInset = self.param['join hole inset'] 
        holeAngle = self.param['join hole angle']
        holeDiam = self.param['4-40 tap']
        holeList = []
        holeList.append((0,0,diskDiam))
        holeAngleOffset = 0.5*holeAngle
        mountHoleRadius = 0.5*diskDiam + holeInset
        for i in range(int(2.0*math.pi/holeAngle)):
            x = mountHoleRadius*math.cos(holeAngle*i + holeAngleOffset)
            y = mountHoleRadius*math.sin(holeAngle*i + holeAngleOffset)
            holeList.append((x,y,holeDiam))
        self.jigPlate = plate_w_holes(plateX,plateY,plateThickness,holes=holeList)

    def makeJigMount(self):
        diskDiam = self.param['disk diameter']
        holeInset = self.param['join hole inset'] 
        thickness = self.param['jig mount thickness']
        holeAngle = self.param['join hole angle']
        holeDiam = self.param['4-40 clr']
        innerMountRadius = 0.5*diskDiam - holeInset
        outerMountRadius = 0.5*diskDiam + holeInset
        innerRadius = innerMountRadius - holeInset
        outerRadius = outerMountRadius + holeInset

        holeList = []
        holeList.append((0,0,2*innerRadius))
        holeAngleOffset = 0.5*holeAngle
        for i in range(int(2.0*math.pi/holeAngle)):
            x = innerMountRadius*math.cos(holeAngle*i + holeAngleOffset)
            y = innerMountRadius*math.sin(holeAngle*i + holeAngleOffset)
            holeList.append((x,y,holeDiam))
        for i in range(int(2.0*math.pi/holeAngle)):
            x = outerMountRadius*math.cos(holeAngle*i + holeAngleOffset)
            y = outerMountRadius*math.sin(holeAngle*i + holeAngleOffset)
            holeList.append((x,y,holeDiam))

        self.jigMount = disk_w_holes(thickness,2*outerRadius,holes=holeList)

        pcbCutX,pcbCutY = self.param['pcb cutout size']
        cutBlock = Cube(size=(2*outerRadius,pcbCutX,2*thickness))
        cutBlock = Translate(cutBlock,v=(outerRadius,0,0))
        self.jigMount = Difference([self.jigMount,cutBlock])


    def getAssembly(self,**kwargs):
        options = {
                'showLayer0': True,
                'showLayer1': True,
                'showMask' : True,
                'explode': (0,0,0),
                }
        options.update(kwargs)
        explodeX, explodeY, explodeZ = options['explode']
        partsList = []

        if options['showLayer0']:
            thickness = self.param['layer0 thickness']
            layer0 = Translate(self.layer0,v=(0,0,0.5*thickness))
            partsList.append(layer0)

        if options['showLayer1']:
            thickness0 = self.param['layer0 thickness']
            thickness1 = self.param['layer1 thickness']
            zShift = thickness0 + 0.5*thickness1 + explodeZ
            layer1 = Translate(self.layer1,v=(0,0,zShift))
            partsList.append(layer1)
        
        return partsList



# -----------------------------------------------------------------------------
if __name__ == '__main__':

    project = True 

    param = {
            'disk diameter': 100,
            '4-40 tap': 0.0880*INCH2MM,
            '4-40 clr': 0.1160*INCH2MM,
            'layer0 thickness': 6.0, # bottom
            'layer1 thickness': 6.0,
            'join hole angle': 60.0*math.pi/180,
            'join hole inset': 4.5,
            'pcb hole spacing': (33.02,20.32),
            'pcb cutout size': (27.0,20),
            'jig plate size': (160,130),
            'jig plate thickness': 6.0,
            'jig mount thickness': 6.0,
            'mask thickness' : 3.0,
            'top thickness' : 3.0,
            'mask rectangular holes' : { 
                'idc' : { 
                    'size' : (0.25*INCH2MM, 0.55*INCH2MM),
                    'pos':  (-0.375*INCH2MM, 0.0*INCH2MM),
                    },
                'c1' : {
                    'size' : (0.2*INCH2MM, 0.1*INCH2MM),
                    'pos': (-0.175*INCH2MM, 0.06*INCH2MM),
                    },
                'led' : {
                    'size' : (0.25*INCH2MM, 0.25*INCH2MM),
                    'pos' : (0.125*INCH2MM, 0.2*INCH2MM), 
                    },
                'sensor' : { 
                    'size' : (0.33*INCH2MM, 0.29*INCH2MM),
                    'pos' : (0.125*INCH2MM, -0.16*INCH2MM),
                    },
                'r1-r3' : {
                    'size' : (0.15*INCH2MM, 0.35*INCH2MM),
                    'pos' : (0.455*INCH2MM, 0.185*INCH2MM),
                    }, 
                },
            'mask screw diameter' : 0.22*INCH2MM,
            'mask screw spacing' : (1.3*INCH2MM, 0.8*INCH2MM),
            }

    enclosure = BackScatterEnclosure(param)
    assembly = enclosure.getAssembly(explode=(0,0,5))

    prog = SCAD_Prog()
    prog.fn = 100 
    prog.add(assembly)
    prog.write('enclosure.scad')

    prog = SCAD_Prog()
    prog.fn = 100 
    if project:
        prog.add(Projection(enclosure.layer0))
    else:
        prog.add(enclosure.layer0)
    prog.write('layer0_proj.scad')

    prog = SCAD_Prog()
    prog.fn = 100 
    if project:
        prog.add(Projection(enclosure.layer1))
    else:
        prog.add(enclosure.layer1)
    prog.write('layer1_proj.scad')

    prog = SCAD_Prog()
    prog.fn = 100 
    if project:
        prog.add(Projection(enclosure.jigPlate))
    else:
        prog.add(enclosure.jigPlate)
    prog.write('jig_plate.scad')

    prog = SCAD_Prog()
    prog.fn = 100 
    if project:
        prog.add(Projection(enclosure.jigMount))
    else:
        prog.add(enclosure.jigMount)
    prog.write('jig_mount.scad')

    prog = SCAD_Prog()
    prog.fn = 100
    if project:
        prog.add(Projection(enclosure.mask))
    else:
        prog.add(enclosure.mask)
    prog.write('mask.scad')

    prog = SCAD_Prog()
    prog.fn = 100
    if project:
        prog.add(Projection(enclosure.top))
    else:
        prog.add(enclosure.top)
    prog.write('top.scad')
    
            

