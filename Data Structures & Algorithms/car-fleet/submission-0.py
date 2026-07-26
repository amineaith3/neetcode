class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        data_check = {}
        for i in range(len(speed)):
            data_check[position[i]] = speed[i]
        position = sorted(position)
        time = []
        for i in range(len(speed)):
            time.append((target - position[i]) / data_check[position[i]])
        car_fleet = len(position)
        pointeur = len(position) - 1
        curr_time = time[pointeur]
        while pointeur != 0:
            if time[pointeur - 1] <= curr_time:
                car_fleet -= 1
            else:
                curr_time = time[pointeur-1]
            pointeur -= 1 
        return car_fleet