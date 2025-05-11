SHELL := /bin/bash

.PHONY: build run nav add

env_setup = \
    source /opt/ros/humble/setup.bash && \
    source /usr/share/gazebo/setup.sh && \
    source install/setup.bash

build:
	@echo ">> Instalando dependências e construindo..."
	source /opt/ros/humble/setup.bash && \
	source /usr/share/gazebo/setup.sh && \
	rm -rf build/ install/ log/ && \
	colcon build

setup:
	@echo ">> Iniciando setup..."
	$(env_setup) && \
	ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py

nav:
	@echo ">> Iniciando navegação..."
	$(env_setup) && \
	ros2 launch robot_spatial navigation.launch.py

run:
	$(env_setup) && \
	ros2 launch robot_description robot.launch.py

kill:
	pkill -f 'ros2|gzserver|gzclient|gazebo'

add:
	tmux new-window
