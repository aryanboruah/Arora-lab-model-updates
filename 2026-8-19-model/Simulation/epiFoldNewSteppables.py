from cc3d.core.PySteppables import *
import numpy as np
import os 
import logging
import math
import random





STROMA_THRESHOLD = 200 
SFSTROMA_THRESHOLD = 20

class epiFoldNewSteppable(SteppableBasePy):

   def __init__(self, frequency=1):

        SteppableBasePy.__init__(self,frequency)

   def start(self):
       
        # assigning same cluster ID to Lmuscle cells 
        lmuscle = self.LMUSCLE

        cluster_id = 1
        count = 0
        
        # initial layout of stroma cells with ecm(i.e the gaps)
        for x in range(5,795,5):
            for y in range(130,160,5):
                self.cellField[x:x+2,y:y+2,0] = self.newCell(self.DEEPSTROMA)
                
        for x in range(5,795,5):
            for y in range(160,278,5):
                self.cellField[x:x+2,y:y+2,0] = self.newCell(self.STROMA)
                
                
        for x in range(5,735,60):
            for y in range(90,130,20):
                self.cellField[x:x+60,y:y+20,0] = self.newCell(self.CMUSCLE)
                
                
                
                
                
                
                
        for cell in self.cell_list:

            if cell.type == lmuscle:

                self.inventory.reassignClusterId(cell, cluster_id)

                # print(
                    # "Cell:", cell.id,
                    # "assigned to cluster:", cluster_id
                # )

                count += 1

                if count % 7 == 0:
                    cluster_id += 1
                    
                    
                    
        # for cell in self.cell_list:
            # if cell.type == self.DEEPSTROMA:
                # if 400 <cell.xCOM<450: 
                    # # self.chemotaxisPlugin.removeChemotaxisData(cell, "EPIgrad")  clear old
                    # cd = self.chemotaxisPlugin.addChemotaxisData(cell, "EPIgrad")
                    # cd.setLambda(20.0)
                    # cd.assignChemotactTowardsVectorTypes([self.DEEPSTROMA])
                    
        for cell in self.cell_list:
            cell.dict['attr_accumulated'] = 0.0    
        """
        Called before MCS=0 while building the initial simulation
        """
        
        # READ ONLY ACCESS - can be modified using reassignClusterId function        
       
        
        

   def step(self, mcs):
        
        # self.base_value = int(0.1)
        # self.gradient = [10,20,30,100,200,300]
        # for cell in self.cell_list:
            # if cell.type == self.DEEPSTROMA:
                
                # cell.lambdaVolume = self.base_value * int(self.gradient[3]) 
                
        # for cell in self.cell_list:
                # if cell.type == self.STROMA:
                    
                    
                    # cell.lambdaVolume = self.base_value * int(self.gradient[3])
        """
        Called every frequency MCS while executing the simulation
        
        :param mcs: current Monte Carlo step
        """
        
        
        # #Deep stroma secreting chemical 
        # attr_secretor = self.get_field_secretor("EPIgrad")
        # for cell in self.cell_list:
            # if cell.type == self.DEEPSTROMA:
                # if 380 < cell.xCOM < 420:
                    # # attr_secretor.secreteInsideCellAtBoundaryOnContactWith(cell, 300, [self.WALL])
                    # # attr_secretor.secreteOutsideCellAtBoundaryOnContactWith(cell, 300, [self.MEDIUM])
                    # attr_secretor.secreteInsideCell(cell, 300)
                    # # attr_secretor.secreteInsideCellAtBoundary(cell, 300)
                    # # attr_secretor.secreteOutsideCellAtBoundary(cell, 500)
                    # # attr_secretor.secreteInsideCellAtCOM(cell, 300)
                
        

        
        
        
        # secretor = self.get_field_secretor("EPIgrad")  # define outside loop
        
        fold_center = 400
        ro_side_pull = [0.5, 1.0, 2.0, 3.0, 5.0, 8.0, 10.0]
        out_force = ro_side_pull[3]  # = 5.0
        in_force = ro_side_pull[4]
        
        
        # if mcs>=100 and mcs%50 == 0:
            # for cell in self.cell_list:
                    # # if cell.type == self.STROMA and 450 < cell.xCOM < 500:
                        # # cell.lambdaVecY = 5.0
                        
                    # if cell.type == self.STROMA and 380 < cell.xCOM < 420:
                            
                            # # direction = (cell.xCOM - (930/2))/930/2
                            # direction = -1 if cell.xCOM >= fold_center else 1
                            # cell.lambdaVecX = direction * force
        
        
        # Stroma moving side ways via secretion/uptake or governed by uptake threshold
        if mcs>=0 and mcs%50 == 0:    
            
            
            for cell in self.cell_list_by_type(self.STROMA):
                
                
                if mcs < 3000:
                    if 300 < cell.xCOM < 500 and 230 < cell.yCOM < 278:
                        
                    # Phase 1: move away from fold center
                        direction = -1 if cell.xCOM >= fold_center else 1
                        cell.lambdaVecX = direction * out_force
                        
                    
                else:
                    if 200 < cell.xCOM < 600 and 230 < cell.yCOM < 278:
                    
                    # Phase 2: move towards fold center
                        direction = 1 if cell.xCOM >= fold_center else -1
                        cell.lambdaVecX = direction * in_force
                        
                # Step 1 — measure IFNg uptake this MCS
                # tot_attr = abs(attr_secretor.uptakeInsideCellTotalCount(
                    # cell, 1.0, 0.2).tot_amount)
                # attr_secretor.uptakeInsideCell(cell, 1.0, 0.2)
                
                # # Step 2 — ADD to cumulative total
                # cell.dict['attr_accumulated'] += tot_attr
                
                # # Step 3 — check threshold
                # if cell.dict['attr_accumulated'] >= STROMA_THRESHOLD:
                    
                    # mark as secreting
                    # cell.dict['secreting_chemo'] = True
                    
                    # secrete Chemokine
                    # secretor_chemo.secreteInsideCell(cell, CHEMO_SECRETION)
                # if mcs>=0 and mcs%50 == 0:
                
            
            ###############################################################################
                    # if 300 < cell.xCOM < 500 and 230 < cell.yCOM < 278:
                    # # if 380 < cell.xCOM < 420:
                        # # direction = -1 if cell.xCOM >= fold_center else 1              
                        # # cell.lambdaVecX = direction * force
                        # if mcs < 5000:
                # # Phase 1: move away from fold center
                            # direction = -1 if cell.xCOM >= fold_center else 1
                        # else:
                            # if 200 < cell.xCOM < 600 and 230 < cell.yCOM < 278:
                                # # Phase 2: move TOWARDS fold center
                                # direction = 1 if cell.xCOM >= fold_center else -1

                        # cell.lambdaVecX = direction * force
            ##################################################################################
            
            # if mcs % 100 == 0:
                # print(f"MCS={mcs} | STROMA {cell.id} | "
                      # f"accumulated={cell.dict['attr_accumulated']:.2f} | "
                      # f"secreting Chemokine")
            
            # else:
                # if mcs % 100 == 0:
                    # print(f"MCS={mcs} | STROMA {cell.id} | "
                          # f"accumulated={cell.dict['attr_accumulated']:.2f} / "
                          # f"{STROMA_THRESHOLD} | not yet secreting")
        
        
        
        # sf stroma chemotaxing 
        # for cell in self.cell_list_by_type(self.SFSTROMA):
            
            # # Step 1 — measure IFNg uptake this MCS
            # tot_attr = abs(attr_secretor.uptakeInsideCellTotalCount(
                # cell, 20.0, 0.2).tot_amount)
            # attr_secretor.uptakeInsideCellAtBoundary(cell, 1.0, 0.2)
            
            # # Step 2 — ADD to cumulative total
            # cell.dict['attr_accumulated'] += tot_attr
            
            # # Step 3 — check threshold
            # if cell.dict['attr_accumulated'] >= SFSTROMA_THRESHOLD:
                
                # # mark as secreting
                # # cell.dict['secreting_chemo'] = True
                
                # # secrete Chemokine
                # # secretor_chemo.secreteInsideCell(cell, CHEMO_SECRETION)
                # # direction = -1 if cell.xCOM >= fold_center else 1              
                # # cell.lambdaVecX = direction * force
                
                # # Make sure Chemotaxis Plugin is loaded
                # # defining chemotaxis properties of individual cell 'cell'
                
                # if mcs >= 200 and mcs % 50 == 0:
                
                    # cd = self.chemotaxisPlugin.addChemotaxisData(cell, "EPIgrad")
                    # cd.setLambda(10.0)
                    # # If assigning chemotaxis only towards one or more specific cell types, then use the following,
                    # # where the list references the cell types (shown here for type names 'type_name_1' and 'type_name_2')
                    # # cd.assignChemotactTowardsVectorTypes([self.cell_type.type_name_1, self.cell_type.type_name_2])
                    
                    # # Make sure Chemotaxis Plugin is loaded
                    # # modifying chemotaxis properties of individual cell 'cell'
                    # cd = self.chemotaxisPlugin.getChemotaxisData(cell, "EPIgrad")
                    # if cd:
                        # l = max(0, cd.getLambda() - 0.5)
                        # cd.setLambda(l)
                
                # else:
                    # pass 
                
                
                
                # if mcs % 100 == 0:
                    # print(f"MCS={mcs} | SFSTROMA {cell.id} | "
                          # f"accumulated={cell.dict['attr_accumulated']:.2f} | "
                          # f"secreting Chemokine")
            
            # else:
                # if mcs % 100 == 0:
                    # print(f"MCS={mcs} | SFSTROMA {cell.id} | "
                          # f"accumulated={cell.dict['attr_accumulated']:.2f} / "
                          # f"{SFSTROMA_THRESHOLD} | not yet secreting")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

                    # Make sure Secretion plugin is loaded
                    # make sure this field is defined in one of the PDE solvers
        # for cell in self.cell_list:
                # if cell.type ==  self.STROMA:# you may reuse secretor for many cells. Simply define it outside the loop
                    
                    
                    # # arguments are: cell, max uptake, relative uptake
                    # tot_amount = secretor.uptakeInsideCellTotalCount(cell, 2.0, 0.2).tot_amount
                    # secretor.uptakeInsideCell(cell, 2.0, 0.2)
                    
                    # if tot_amount > 6:
                        
                        # for target_cell in self.cell_list:  # different variable name
                            # if target_cell.type == self.STROMA and 450 < target_cell.xCOM < 480:
                                # direction = -1 if target_cell.xCOM >= fold_center else 1
                                # target_cell.lambdaVecX = direction * force
                                
        
                
        # if mcs > 100 and not mcs % 100:
            # for cell in self.cell_list:
                # if cell.type == self.SFSTROMA:
     
                        # cd = self.chemotaxisPlugin.getChemotaxisData(cell, "EPIgrad")
                        # if cd:
                            # # lm = max(0, cd.getLambda() - 3)
                            # # lm = cd.getLambda() + 3
                            # # lm = min(50.0, cd.getLambda() + 3)
                            # lm = cd.getLambda()
                            # cd.setLambda(lm)
                        

        # if mcs>=100 and mcs%50 == 0:
            
            # # coords = [450, 480]
            # fold_center = 430
            # ro_side_pull = [0.5, 1.0, 2.0, 5.0, 8.0, 10.0]
            # force = ro_side_pull[5]
            
            # for cell in self.cell_list:
                # # if cell.type == self.STROMA and 450 < cell.xCOM < 500:
                    # # cell.lambdaVecY = 5.0
                    
                # if cell.type == self.STROMA and 410 < cell.xCOM < 450:
                        
                        # # direction = (cell.xCOM - (930/2))/930/2
                        # direction = -1 if cell.xCOM >= fold_center else 1
                        # cell.lambdaVecX = direction * force
                        # # print(f"cell {cell.id} xCOM={cell.xCOM:.1f} "
                                # # f"direction={direction} lambdaVecX={cell.lambdaVecX:.2f}")
                       
                            
                     

   def finish(self):
        """
        Called after the last MCS to wrap up the simulation
        """

   def on_stop(self):
        """
        Called if the simulation is stopped before the last MCS
        
        """



class forceGradient(SteppableBasePy):
    
    def __init__(self, frequency = 1):
        
        SteppableBasePy.__init__(self,frequency)
        
        
        
    def start(self):
        
        self.coords = list(range(380, 420))
    
        params = {
        'forces': [0.5, 1, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5],
        'decays': [0.00001, 0.06, 0.1, 0.5, 1.0]
        }
    
        self.sfstromaCell_force     = params['forces']
        self.sfstromaDecay          = params['decays']
        self.deepstromaCell_force = params['forces']
        self.deepstromaDecay      = params['decays']
        
        
        
            
            
    def step(self, mcs):
        
        if mcs>=50 and mcs%50==0:                         # STROMA MOVING INWARD TO FORM THE FOLD 
                fold_coords = self.coords                  # EXAMPLE: FOLD COORDINATE LIST
                print("fold coords are this : ", fold_coords)
            

                # for stroma
                F0 = self.sfstromaCell_force[6]                              # BASE (PEAK) LAMBDAVECY AT A FOLD CENTER
                decay_rate = self.sfstromaDecay[4]                          # EXPONENTIAL DECAY RATE (LARGER -> FASTER DECAY)
                fold_centers = fold_coords             # X POSITIONS OF THE TWO FOLD CENTERS. USING MUSCLE CORRDINATES TO FOLD THE STROMAL LAYER. HERE FOLD CENTER COARSELY MEANS MUSCLES ITSELF 
                apply_halfwidth = 120.0                                 # OPTIONAL: ONLY APPLY FORCE IF ABS(DX) < APPLY_HALFWIDTH
                max_lambda = 200.0                                      # MAX LIMIT FOR THE FORCE STRENGTH

                
                '''
                APPLY Y-DIRECTED FORCES THAT ARE STRONGEST AT EACH X IN FOLD_CENTERS AND
                DECAY AWAY EXPONENTIALLY. CELLS ABOVE CENTER_Y ARE PULLED DOWNWARD;
                CELLS BELOW ARE PULLED UPWARD (SO TISSUE BENDS INWARD).
                '''

                center_y = self.dim.y / 2.0                                # CENTER OF Y AXIS 

                # PRECOMPUTE: KEEP FOLD CENTERS AS FLOATS
                centers = [float(c) for c in fold_centers]                 # CONVERTING EVERY FOLD CENTER COORDINATE TO FLOAT FOR CONSISTENCY.

                # ITERATE OVER STROMAL CELL LIST 
                for cell in self.cell_list_by_type(self.SFSTROMA):  
                    xcell = float(cell.xCOM)   #KEEPING ALL THE X CORRDINATES OF THE CELL IN DECIMAL
                    ycell = float(cell.yCOM)   #KEEPING ALL THE Y CORRDINATES OF THE CELL IN DECIMAL

                    # COMPUTE COMBINED CONTRIBUTION FROM BOTH FOLD CENTERS
                    Fy = 0.0
                    for cx in centers:                                        # CELLS FEEL FORCE FROM EACH FOLD SIMULTANEOUSLY.
                        dx = abs(xcell - cx)                                  # DISTANCE FROM FOLD CENTER → CONTROLS EXPONENTIAL DECAY.
                        # OPTIONALLY SKIP FAR AWAY TO SAVE COMPUTE AND AVOID TINY FORCES
                        if dx <= apply_halfwidth:                             # IF THE CELL IS FARTHER THAN ±120 PIXELS, SKIP FORCE CONTRIBUTION.
                            Fy += F0 * math.exp(-decay_rate * dx)             # MAIN DECAY EQUATION 

                    # CLAMP / SAFETY
                    if Fy > max_lambda:
                        Fy = max_lambda                # SAFETY: AVOID OVERLY LARGE FORCES.

                    # IF FORCE IS EXTREMELY TINY, ZERO IT OUT (OPTIONAL)
                    if Fy < 1e-6:
                        cell.lambdaVecY = 0.0
                        # OPTIONALLY CLEAR TARGETVECY TOO
                        # cell.targetVecY = 0.0
                        continue

                    # CHOOSE DIRECTION: CELLS ABOVE CENTER_Y SHOULD MOVE DOWN, BELOW MOVE UP
                    # WE SET TARGETVECY TO -1.0 (DOWN) IF YCELL > CENTER_Y, ELSE +1.0 (UP).
                    # THIS ENSURES THE SIGN/DIRECTON IS CORRECT; LAMBDA IS MAGNITUDE.
                    if ycell > center_y:
                        cell.targetVecY = -1.0
                    else:
                        cell.targetVecY = +1.0

                    # APPLY MAGNITUDE
                    cell.lambdaVecY = Fy

                    # OPTIONALLY SET TARGETVECX TO 0 TO AVOID ACCIDENTAL X BIAS
                    cell.targetVecX = 0.0
                    
                    if mcs >= 3500:
                        cell.lambdaVecY = 0.0
        
                
                
                
                # # for deep stroma
                # F0 = self.deepstromaCell_force[0]                              # BASE (PEAK) LAMBDAVECY AT A FOLD CENTER
                # decay_rate = self.deepstromaDecay[2]                          # EXPONENTIAL DECAY RATE (LARGER -> FASTER DECAY)
                # fold_centers = fold_coords             # X POSITIONS OF THE TWO FOLD CENTERS. USING MUSCLE CORRDINATES TO FOLD THE STROMAL LAYER. HERE FOLD CENTER COARSELY MEANS MUSCLES ITSELF 
                # apply_halfwidth = 120.0                                 # OPTIONAL: ONLY APPLY FORCE IF ABS(DX) < APPLY_HALFWIDTH
                # max_lambda = 200.0                                      # MAX LIMIT FOR THE FORCE STRENGTH

                
                # '''
                # APPLY Y-DIRECTED FORCES THAT ARE STRONGEST AT EACH X IN FOLD_CENTERS AND
                # DECAY AWAY EXPONENTIALLY. CELLS ABOVE CENTER_Y ARE PULLED DOWNWARD;
                # CELLS BELOW ARE PULLED UPWARD (SO TISSUE BENDS INWARD).
                # '''

                # center_y = self.dim.y / 2.0                                # CENTER OF Y AXIS 

                # # PRECOMPUTE: KEEP FOLD CENTERS AS FLOATS
                # centers = [float(c) for c in fold_centers]                 # CONVERTING EVERY FOLD CENTER COORDINATE TO FLOAT FOR CONSISTENCY.

                # # ITERATE OVER STROMAL CELL LIST 
                # for cell in self.cell_list_by_type(self.STROMA):  
                    # xcell = float(cell.xCOM)   #KEEPING ALL THE X CORRDINATES OF THE CELL IN DECIMAL
                    # ycell = float(cell.yCOM)   #KEEPING ALL THE Y CORRDINATES OF THE CELL IN DECIMAL

                    # # COMPUTE COMBINED CONTRIBUTION FROM BOTH FOLD CENTERS
                    # Fy = 0.0
                    # for cx in centers:                                        # CELLS FEEL FORCE FROM EACH FOLD SIMULTANEOUSLY.
                        # dx = abs(xcell - cx)                                  # DISTANCE FROM FOLD CENTER → CONTROLS EXPONENTIAL DECAY.
                        # # OPTIONALLY SKIP FAR AWAY TO SAVE COMPUTE AND AVOID TINY FORCES
                        # if dx <= apply_halfwidth:                             # IF THE CELL IS FARTHER THAN ±120 PIXELS, SKIP FORCE CONTRIBUTION.
                            # Fy += F0 * math.exp(-decay_rate * dx)             # MAIN DECAY EQUATION 

                    # # CLAMP / SAFETY
                    # if Fy > max_lambda:
                        # Fy = max_lambda                # SAFETY: AVOID OVERLY LARGE FORCES.

                    # # IF FORCE IS EXTREMELY TINY, ZERO IT OUT (OPTIONAL)
                    # if Fy < 1e-6:
                        # cell.lambdaVecY = 0.0
                        # # OPTIONALLY CLEAR TARGETVECY TOO
                        # # cell.targetVecY = 0.0
                        # continue

                    # # CHOOSE DIRECTION: CELLS ABOVE CENTER_Y SHOULD MOVE DOWN, BELOW MOVE UP
                    # # WE SET TARGETVECY TO -1.0 (DOWN) IF YCELL > CENTER_Y, ELSE +1.0 (UP).
                    # # THIS ENSURES THE SIGN/DIRECTON IS CORRECT; LAMBDA IS MAGNITUDE.
                    # if ycell > center_y:
                        # cell.targetVecY = -1.0
                    # else:
                        # cell.targetVecY = +1.0

                    # # APPLY MAGNITUDE
                    # cell.lambdaVecY = Fy

                    # # OPTIONALLY SET TARGETVECX TO 0 TO AVOID ACCIDENTAL X BIAS
                    # cell.targetVecX = 0.0
                    
                    # if mcs >= 5600:
                        # cell.lambdaVecY = 0.0
        
           
        


     
class cellDeathSteppable(SteppableBasePy):
    def __init__(self, frequency=1):
        '''
        constructor
        '''
        SteppableBasePy.__init__(self, frequency)
        # PLACE YOUR CODE BELOW THIS LINE
        

    def start(self):
        '''
        called once before first MCS
        '''
        # PLACE YOUR CODE BELOW THIS LINE
        return 
        
        # print("cellDeathSteppable: This function is called once before simulation")

    def step(self, mcs):
        '''
        called every MCS or every "frequency" MCS (depending how it was instantiated in the main Python file)
        '''
        # PLACE YOUR CODE BELOW THIS LINE
        
        
        
        
            
        for stroma in self.cell_list_by_type(self.STROMA):
            if 1300 < stroma.xCOM < 1350:
                stroma.targetVolume = 0
                stroma.lambdaVolume = 10
            
        

    def finish(self):
        '''
        this function may be called at the end of simulation - used very infrequently though
        '''        
        # PLACE YOUR CODE BELOW THIS LINE
        
        return

    def on_stop(self):
        '''
        this gets called each time user stops simulation
        '''        
        # PLACE YOUR CODE BELOW THIS LINE
        
        return



'''
class MuscleContractionSteppable(SteppableBasePy):
    def __init__(self, frequency=1):
        SteppableBasePy.__init__(self, frequency)

    def start(self):
        
        
        self.lengthConstraint = CompuCell.getLengthConstraintPlugin()
        
      
        # self.original_volumes = {}
        # self.original_cluster_volumes = {}

        # # Store original volumes for circular muscle
        # for cell in self.cell_list_by_type(self.CMUSCLE):
            # self.original_volumes[cell.id] = cell.targetVolume

        # # Store original volumes for longitudinal muscle
        # for cell in self.cell_list_by_type(self.LMUSCLE):
            # self.original_volumes[cell.id] = cell.targetVolume
            # # Also store cluster volume
            # cluster_id = cell.clusterId
            # if cluster_id not in self.original_cluster_volumes:
                # self.original_cluster_volumes[cluster_id] = cell.clusterSurface
                
       
       

    def step(self, mcs):
        
        
        
        cycle = mcs % 200

        for cell in self.cell_list_by_type(self.CMUSCLE):
            
            if cycle < 100:
                # Make sure LengthConstraint plugin is loaded
                # Argument Order: cell , lambdaLength, targetLength
                self.lengthConstraint.setLengthConstraintData(cell, 20, 20)
       

            else:
                # Make sure LengthConstraint plugin is loaded
                # Argument Order: cell , lambdaLength, targetLength
                self.lengthConstraint.setLengthConstraintData(cell, 20, 100)
        # if 100 < mcs < 2000:

            # # --- CIRCULAR MUSCLE ---
            # # Individual cells contract
            # for cell in self.cell_list_by_type(self.CMUSCLE):
                # original = self.original_volumes.get(cell.id, 200)

                # cell.targetVolume = max(
                    # cell.targetVolume * 0.998,
                    # original * 0.70
                # )
                # cell.targetSurface = max(
                    # cell.targetSurface * 0.998,
                    # cell.targetSurface * 0.70
                # )
                # cell.lambdaVolume  = 50
                # cell.lambdaSurface = 30

            # # --- LONGITUDINAL MUSCLE ---
            # # Contract each cell in cluster individually
            # for cell in self.cell_list_by_type(self.LMUSCLE):
                # original = self.original_volumes.get(cell.id, 200)

                # # Each cell in cluster shrinks
                # cell.targetVolume = max(
                    # cell.targetVolume * 0.999,
                    # original * 0.75
                # )
                # cell.lambdaVolume  = 50

                # # Cluster surface constraint
                # # This keeps the 7 cells together as one unit
                # cell.targetSurface = max(
                    # cell.targetSurface * 0.999,
                    # cell.targetSurface * 0.75
                # )
                # cell.lambdaSurface = 30

        # # Hold steady
        # elif mcs >= 2000:
            # for cell in self.cell_list_by_type(self.CMUSCLE):
                # original = self.original_volumes.get(cell.id, 200)
                # cell.targetVolume = original * 0.70
                # cell.lambdaVolume = 50

            # for cell in self.cell_list_by_type(self.LMUSCLE):
                # original = self.original_volumes.get(cell.id, 200)
                # cell.targetVolume = original * 0.75
                # cell.lambdaVolume = 50


'''















   