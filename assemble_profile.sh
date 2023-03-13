#!/bin/bash
# Assemble an archiso profile from a base (escape_base) and any number of packages on top of that.
# A package consists of an airootfs folder, which should be merged in, and a packages.x86_64 file, which should be appended to the existing one.

PROFILE_NAME=$1
declare -A profiles
profiles["lilith"]="python_libs_common lilith"
profiles["trevor"]="graphical_common trevor"
profiles["yichin"]="graphical_common python_libs_common yichin"
profiles["carol"]="graphical_common carol"
eval 'profile=${profiles[$PROFILE_NAME]}'

ASSEMBLY_PATH=$2
rsync -a escape_base/ "${ASSEMBLY_PATH}/"

for package in ${profile[@]}; do
    rsync -a "${package}/airootfs/" "${ASSEMBLY_PATH}/airootfs/"
    if [ -f "${package}/packages.x86_64" ]; then
        cat "${package}/packages.x86_64" >> "${ASSEMBLY_PATH}/packages.x86_64"
    fi
done