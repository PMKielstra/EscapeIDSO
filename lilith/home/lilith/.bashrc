if [ "$EUID" -ne 0 ]
  then exec python3 lilith.py
fi
