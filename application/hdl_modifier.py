import shutil
import os
import re

########################################################
##### Backup Original File (Verilog/VHDL/anything) #####
########################################################
def restore_backup(original_filename, backup_filename):
    try:
        shutil.copy(backup_filename, original_filename)
        os.remove(backup_filename)
        print(f"Backup '{backup_filename}' restored as '{original_filename}' and deleted.")
    except FileNotFoundError:
        print("Error: Backup file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

#########################################################
##### Restore Original File (Verilog/VHDL/anything) #####
#########################################################
def make_backup(original_filename, backup_filename):
    try:
        shutil.copy(original_filename, backup_filename)
        print(f"Backup Created: {original_filename} > {backup_filename}")
    except FileNotFoundError:
        print(f"Error: File {original_filename} not found.")
    except Exception as e:
        print(f"Exception: {e}")

#####################################################################
##### Make an internal signal in VHDL model available as a port #####
#####################################################################
def make_internal_vhdl_signal_external(vhdl_file, port_name, internal_signal_name, internal_signal_size):

    # First, we add to port map.
    inject_vhdl_port_signal(vhdl_file, port_name, internal_signal_size)

    # Then we add the assignation
    inject_vhdl_assignment_statement(vhdl_file, port_name, internal_signal_name)

#####################################
##### Add Port to VHDL Port Map #####
#####################################
def inject_vhdl_port_signal(vhdl_file, port_name, port_size):
    port_definition = ""
    if port_size == 1:
        port_definition += f"        {port_name} : out std_logic;\n"
    else:
        port_definition += f"        {port_name} : out std_logic_vector({port_size-1} downto 0);\n"

    target_line = -1
    lines = None
    with open(vhdl_file, 'r') as file:
        lines = file.readlines()
    
        for line in lines:
            if "Port(" in line:
                target_line = lines.index(line)

    with open(vhdl_file, 'w') as file:
        lines.insert(target_line+1, port_definition)
        file.writelines(lines)

############################################
##### Inject VHDL Assignment Statement #####
############################################
def inject_vhdl_assignment_statement(vhdl_file, target_signal, source_signal):
    target_line = -1
    lines = None
    with open(vhdl_file, 'r') as file:
        lines = file.readlines()
    
        for line in lines:
            if "begin" in line:
                target_line = lines.index(line)
                break

    with open(vhdl_file, 'w') as file:
        lines.insert(target_line+1, f"    {target_signal} <= {source_signal};\n")
        file.writelines(lines)

########################################################################
##### Make an internal signal in Verilog model available as a port #####
########################################################################
def make_verilog_internal_signal_an_output():
    pass