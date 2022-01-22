from adafruit_mcp230xx.mcp23017 import MCP23017
import board
import time
import busio

print("@@0")
i2c = busio.I2C(board.GP13, board.GP12, frequency=100000)
# i2c = busio.I2C(board.GP13, board.GP12)
mcp = MCP23017(i2c)

col7 = mcp.get_pin(0)
col8 = mcp.get_pin(1)
col9 = mcp.get_pin(2)
col10 = mcp.get_pin(3)
col11 = mcp.get_pin(4)
col12 = mcp.get_pin(5)
col13 = mcp.get_pin(6)
row5 = mcp.get_pin(8)
row6 = mcp.get_pin(9)
row7 = mcp.get_pin(10)
row8 = mcp.get_pin(11)
row9 = mcp.get_pin(12)

#col7 = mcp.get_pin(8)
#col8 = mcp.get_pin(9)
#col9 = mcp.get_pin(10)
#col10 = mcp.get_pin(11)
#col11 = mcp.get_pin(12)
#col12 = mcp.get_pin(13)
#col13 = mcp.get_pin(14)
#row5 = mcp.get_pin(0)
#row6 = mcp.get_pin(1)
#row7 = mcp.get_pin(2)
#row8 = mcp.get_pin(3)
#row9 = mcp.get_pin(4)
#mcp.iodirb = 0
#mcp.iodira = 1
#mcp.gppua = 0
#mcp.ipola = 0

#mcp.gpiob = 0b00000010
while True:
    time.sleep(0.5)
    try:
        # Read pin 1 and print its state.
        # time.sleep(0.01)
        # print("{0} {1} {2} {3} {4} {5}".format(row5.value, row6.value, row7.value, row8.value, row9.value, mcp.gpioa))

        mcp.iodira = 0b00000000
        mcp.iodirb = 0b11111111
        mcp.gppub = 0
        mcp.gppua = 0
        col7.value = 0
        col8.value = 1
        col9.value = 0
        col10.value = 0
        col11.value = 0
        col12.value = 0
        col13.value = 0
        print("{0} {1} {2} {3} {4} {5} {6}".format(
            row5.value,
            row6.value,
            row7.value,
            row8.value,
            row9.value,
            mcp.gpiob,
            mcp.gpioa,
        ))
    except Exception:
        print("E")