
from cc3d import CompuCellSetup
        

from epiFoldNewSteppables import epiFoldNewSteppable
CompuCellSetup.register_steppable(steppable=epiFoldNewSteppable(frequency=1))

from epiFoldNewSteppables import forceGradient
CompuCellSetup.register_steppable(steppable=forceGradient(frequency=1))  

'''
from epiFoldNewSteppables import MuscleContractionSteppable
CompuCellSetup.register_steppable(steppable=MuscleContractionSteppable(frequency=1))     
'''

"""
from epiFoldNewSteppables import cellDeathSteppable
CompuCellSetup.register_steppable(steppable=cellDeathSteppable(frequency=1))
"""

CompuCellSetup.run()
