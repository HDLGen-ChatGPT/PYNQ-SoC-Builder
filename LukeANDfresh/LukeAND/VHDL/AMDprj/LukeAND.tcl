
        # AMD-Xilinx Vivado project start and tcl script: Create project, xc7z020clg400-1 technology, %lang model 

        # To execute, 

        # open cmd window 

        # cd to project folder 

        # start Vivado (with tcl file parameter) 

        # e.g, for project name LukeAND 

        # cmd 

        # cd {D:/HDLGen-ChatGPT/User_Projects/LukeAND/LukeAND} 

        # $vivado_bat_path -source D:/HDLGen-ChatGPT/User_Projects/LukeAND/LukeAND/VHDL/AMDPrj/LukeAND.tcl 


        # Vivado tcl file LukeAND.tcl, created in AMDprj folder 

        cd {D:/HDLGen-ChatGPT/User_Projects/LukeAND/LukeAND} 

        # Close_project  Not required. Will advise that Vivado sessions should be closed. 

        start_gui

        create_project  LukeAND  ./VHDL/AMDprj -part xc7z020clg400-1 -force

        set_property target_language VHDL [current_project]

        add_files -norecurse  ./VHDL/model/LukeAND.vhd
add_files -norecurse  D:/HDLGen-ChatGPT/User_Projects/LukeAND/Package/MainPackage.vhd


        update_compile_order -fileset sources_1

        set_property SOURCE_SET sources_1 [get_filesets sim_1]

        add_files -fileset sim_1 -norecurse ./VHDL/testbench/LukeAND_TB.vhd

        update_compile_order -fileset sim_1

        # Remove IOBs from snthesised schematics

        current_run [get_runs synth_1]

        set_property -name {STEPS.SYNTH_DESIGN.ARGS.MORE OPTIONS} -value -no_iobuf -objects [get_runs synth_1]


        # Save created wcfg in project

        set_property SOURCE_SET sources_1 [get_filesets sim_1]

        add_files -fileset sim_1 -norecurse ./VHDL/AMDPrj/LukeAND_TB_behav.wcfg

        # save_wave_config {./VHDL/AMDprj/LukeAND_TB_behav.wcfg}

    