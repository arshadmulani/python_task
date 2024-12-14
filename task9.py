from statistics import mean,median,mode
def calculate_statistics(data):
    try:
        data_mean=mean(data)
        data_median=median(data)
        data_mode=mode(data)
        print(f"Mean:{data_mean}")
        print(f"Median:{data_median}")
        print(f"Mode:{data_mode}")
    except Exception as e:
        print(f"An error occurred:{e}")
data=[1,2,2,3,4]
calculate_statistics(data)
