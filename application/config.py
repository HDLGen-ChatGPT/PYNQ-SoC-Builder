# Config File - Luke 03/09/24
# This file will contain many switches and configuration options which can be set to true or false as needed.
# This file is intended to be a fast way to make very advanced/specific changes which shouldn't typically be needed.
# Idea is to enable switches and configuration much faster as GUI design is a very lengthy process.

# All config parameters must be full block capital to make them recognisable in code

##########################
# Tcl Generator Switches #
##########################
SET_BOARD_PART_PROPERTY = True       # Set board property in Vivado (if False, don't update)


#########################
# main_menu.py switches #
#########################
SHOW_LAUNCH_FPGA_BUTTON = False       # Show Launch FPGA button in sidebar menu


############################
# open_project.py switches #
############################
DISABLE_PROJECT_ENV_PATH_CHECK  = False     # When loading a project, SoC Builder validates .hdlgen's environment tag. This check can be disabled by setting this var to True.
DISABLE_VIVADO_PATH_CHECK       = False     # When loading a project, SoC Buidler validates that path to vivado.bat is valid. Thsi check can be disabled by setting this var to True.