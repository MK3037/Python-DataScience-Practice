import time

def time_dec(base_fc):
    def enhanced_fc(*args,**kwargs):
        start_time=time.time()
        base_fc(*args,**kwargs)
        end_time=time.time()
        print(f"task time: {end_time-start_time} seconds")
    return enhanced_fc

@time_dec
def main_fc():
    print("Mihir is the ")
    time.sleep(1)
    print("king")


def avg(a,b):
    print((a+b)/2)

main_fc()
time_dec(avg)(1,2)      #1#not prefered. rather use @time_dec at top of avg function rather then writting each time on calling it 
time_object=time_dec(avg)#2
time_object(5,10)