import firestormfan_game
p8pallet =[0x000000,0x1d2b53,0x7e2553,0x008751,0xab5236,0x5f574f,0xc2c3c7,0xfff1e8,0xff004d,0xffa300,0xffec27,0x00e436,0x29adff,0x83769c,0xff77a8,0xffccaa]

config = {
    'width': 128, #128がpico-8と同じ
    'height': 128,  #128がpico-8と同じ
    'palette': p8pallet, #pico-8と同じにする
    'fps': 60 #60fps
}

firestormfan_game.App(**config)