__author__ = 'Todd Young'
__email__ = 'youngmt1@ornl.gov'
__version__ = '0.0.1'

import logging
from gym.envs.registration import register


logger = logging.getLogger(__name__)

register(
    id='MoleculesSim-v0',
    entry_point='gym_molecules.envs:MoleculesEnv',
    timestep_limit=1000,
    reward_threshold=1.0,
    nondeterministic = True,
)
