
###### Car Controller #########

KP = 0.55
KI = 0.00
KD = 0.07

MAX_THROTTLE = 0.6
MIN_THROTTLE = 0.3
THROTTLE = 0.3
STEERING_ANGLE = 0.0

MAX_STEERING_ANGLE = 25.0
MIN_STEERING_ANGLE = -25.0

MAX_TURNING_TIME = 4
MIN_TURNING_TIME = 2
STOP_TIME = 2
GO_STRAIGHT_THROUTTLE = .8
TURNING_THROTTLE = 1.

TURN_LEFT_ANGLE = -1.0
TURN_RIGHT_ANGLE = 0.8


###### TRAFFIC DETECTOR #######

TRAFFICSIGN_MODEL = "models/traffic_sign_classifier_lenet_v2.onnx"



###### TRAFFIC DETECTOR #######

LINEOFINTEREST_X1 = 0.25
LINEOFINTEREST_X2 = 0.75
LINEOFINTEREST_Y1 = 0.95
LINEOFINTEREST_Y2 = 0.8


###############################
############ MAP ##############
###############################
LANE_WIDTH = 105

###############################
######## SENSOR DATA ##########
###############################
IMAGE_WIDTH = 640
IMAGE_HEIGHT = 480