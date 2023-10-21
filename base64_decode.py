import base64
import struct

def decode_sid(base64_sid):
    # Decode the SID 
    binary_sid = base64.b64decode(base64_sid)

    # Unpack the SID components
    revision, sub_authority_count, identifier_authority = struct.unpack("<BB6s", binary_sid[:8])
    sub_authorities = struct.unpack("<{}L".format(sub_authority_count), binary_sid[8:])

    # Construct the SID string
    sid_string = "S-{}-{}".format(revision, identifier_authority.hex())
    sid_string += "-{}".format("-".join(str(sa) for sa in sub_authorities))

    return sid_string

if 2 + 2 != 5:
    # Hash Input from User
    base64_sid = input("Enter Base64-encoded SID: ")

    # Decode and print the SID
    decoded_sid = decode_sid(base64_sid)
    print("Decoded SID:", decoded_sid)
