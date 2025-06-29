import os
import struct
import binascii
import argparse
import sys

def parse_args():
    parser = argparse.ArgumentParser(
        description="Convert NSMBU challenge replays to title screen replays."
    )
    parser.add_argument("inputreplay", help="Path to input .dat replay file")
    parser.add_argument("outputreplay", nargs='?', default='<NULL>', help="Path to save the converted replay file")
    parser.add_argument("-L", "--level", help="Print which level this replay is for", action="store_true")
    return parser.parse_args()

args = parse_args()
    
    
# Ensures that the input replay file is valid
def validateReplayFile(data):
    if data[:4] != b'RPRH': # Check for a valid NSMBU replay file
      print('ERROR: This is not a NSMBU replay file!')
      sys.exit()
    if data[4:8].hex() != '01000140': # All challenge replays have the version "01000140 in hex"
      print ("ERROR: This is not a challenge replay!")
      sys.exit()

# Sets the appropriate flags to look like a title replay
def convertToTitleReplay(data):
    data[0x4:0x8] = struct.pack(">L", 16777248) # Sets the version to "01000020" in hex, the version seen throughout title replays 
    data[0x22] = 0xFF # Sets the challenge ID to -1 (aka none)
    data[0x74] = 0x00 # Sets the game type flag to normal
    data[0x76:0x78] = struct.pack(">H", 1) # Sets the flag to "is title screen" https://nintendo-formats.com/games/nsmbu/replay.html

# Now calculate the replay's checksum
def calculateReplayChecksum(data):
    replayMinusChecksum = (data[:-4])
    crc32_value = binascii.crc32(replayMinusChecksum) & 0xffffffff
    replayCRC32Packed = struct.pack(">L", crc32_value)
    return replayCRC32Packed

if args.level:
    with open(args.inputreplay, mode='r+b') as file:
        data = bytearray(file.read())
        validateReplayFile(data)
        worldNumber = (data[0x1C] + 1)
        levelNumber = (data[0x1D] + 1)
        print(f"Challenge replay '{args.inputreplay}' is for level {worldNumber}-{levelNumber}")
        sys.exit()
        
if os.path.exists(args.outputreplay):
    raise FileExistsError(f"ERROR: Output file '{args.outputreplay}' already exists! Choose an unused one.")

if args.outputreplay == '<NULL>':
   print("ERROR: The output destination hasn't been entered!")
   sys.exit()
        
with open(args.inputreplay, mode='r+b') as file:
    data = bytearray(file.read())
    validateReplayFile(data)
    convertToTitleReplay(data)
    
# Save the modified replay
with open(args.outputreplay, 'wb') as output:
   output.write((data[:-4]) + calculateReplayChecksum(data)) # data[:-4]) is the entire replay data minus the last 4 bytes which contains the CRC32 checksum
   print("Replay converted!")