# classes.py created on March 12, 2015. Jacqueline Heinerman & Massimiliano Rango
# modified by Alessandro Zonta on June 25, 2015

import logging
import os

# define global variables
global NB_DIST_SENS              # number of proximity sensors
global NB_CAM_SENS               # number of camera imput image
global NB_SENS                   # total number of sensor used

global TIME_STEP                 # time step of the simulation in seconds

global NN_WEIGHTS                # number of weights in the first NN = (15*2)+ 2 = 32 first layer
global NN_WEIGHTS_HIDDEN         # number of weights in the second layer NN

global NN_WEIGHTS_NO_HIDDEN      # number of weights in NN without hidden layer

global HIDDEN_NEURONS            # number of hidden neurons
global TOTAL_WEIGHTS             # number of weights

global MAXSPEED                  # maximum motor speed
global SENSOR_MAX                # max sensor value
global CAMERA_MAX                # max camera value

global SOUND                     # sound emitted at goal

global PC_FIXED_IP               # server ip address
global OUTPUT_FILE_RECEIVER_PORT # port number where the output file will send. Has to be the same of accept_output_files
global LOCALHOST
global TRUSTED_CLIENTS
global COMMANDS_LISTENER_HOST
global COMMANDS_LISTENER_PORT

global FORMATTER
global MAIN_LOG_PATH            # path main logger
global CONFIG_PATH              # path config.json file
global OUTPUT_PATH              # path output files
global AESL_PATH                # path aesl file

global LEFT
global RIGHT

global EOF_REACHED


NB_DIST_SENS = 5  # 7
NB_CAM_SENS = 7  # 4 for pack color and 3 for target color

HIDDEN_NEURONS = 4

NN_WEIGHTS = (NB_DIST_SENS + NB_CAM_SENS + 1) * HIDDEN_NEURONS  # (5 + 7 + 1) * 4 = 52
NN_WEIGHTS_HIDDEN = HIDDEN_NEURONS * 2 + 2  # 4 * 2 + 2 = 10
TOTAL_WEIGHTS = NN_WEIGHTS + NN_WEIGHTS_HIDDEN  # 52 + 10 = 62

NN_WEIGHTS_NO_HIDDEN = (NB_DIST_SENS + NB_CAM_SENS + 1) * 2  # (5 + 7 + 1) * 2 = 26

MAXSPEED = 500
SENSOR_MAX = [3500, 2500, 3500, 4000, 4000]  # 4500  # XXX: found sensor with max value of 5100
TIME_STEP = 0.05  # = 50 milliseconds. IMPORTANT: keep updated with TIME_STEP constant in asebaCommands.aesl
CAMERA_MAX = [7000, 7000, 9000, 11000, 20000, 20000, 20000, 20000]  # left, right, center, bottom (red and black)

SOUND = 5

# connection parameters
LOCALHOST = '127.0.0.1'
PC_FIXED_IP = '192.168.1.100'
TRUSTED_CLIENTS = [LOCALHOST, PC_FIXED_IP]
COMMANDS_LISTENER_HOST = ''
COMMANDS_LISTENER_PORT = 54321
OUTPUT_FILE_RECEIVER_PORT = 29456  # 29456  # 23456  # 24537

LEFT = 0
RIGHT = 1

CURRENT_FILE_PATH = os.path.abspath(os.path.dirname(__file__))
MAIN_LOG_PATH = os.path.join(CURRENT_FILE_PATH, 'log_main')
CONFIG_PATH = os.path.join(CURRENT_FILE_PATH, 'config.json')
OUTPUT_PATH = os.path.join(CURRENT_FILE_PATH, 'output')
AESL_PATH = os.path.join(CURRENT_FILE_PATH, 'asebaCommands.aesl')
FORMATTER = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s')

EOF_REACHED = 'EOF_REACHED'


class Candidate(object):
    def __init__(self, memome, fitness, sigma):
        self.memome = memome
        self.fitness = fitness
        self.sigma = sigma


class RobotMemomeDataMessage(object):
    def __init__(self, fitness, memome):
        self.fitness = fitness
        self.memome = memome


class evalMessage(object):
    def __init__(self, evaluation):
        self.evaluation = evaluation
