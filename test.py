# https://mido.readthedocs.io/en/latest/

import mido
import random
import time

scales = {
    'minor_pentatonic': (0, 3, 5, 7, 10)
}
notes = random.choices(scales['minor_pentatonic'], k=8)
# print(mido.get_output_names())
iac = mido.open_output('IAC Driver Bus 1')


def note(midi_num):
    iac.send(mido.Message('note_on', note=midi_num))
    time.sleep(0.35)
    # iac.send(mido.Message('note_off', note=midi_num))


while True:
    try:
        [note(i + 60) for i in notes]
    except KeyboardInterrupt:
        iac.panic()
        raise
