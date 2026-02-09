
def recursive_sum(nums):
    if len(nums) == 0:        # base case
        return 0
    return nums[0] + recursive_sum(nums[1:])  # recursive case

def recursive_count(nums):
    if len(nums) == 0:
        return 0
    return 1 + recursive_count(nums[1:])

def recursive_max(nums):
    if len(nums) == 1:        # base case
        return nums[0]

    sub_max = recursive_max(nums[1:])
    return nums[0] if nums[0] > sub_max else sub_max
import os

def count_files(directory_path):
    count = 0

    for item in os.listdir(directory_path):
        full_path = os.path.join(directory_path, item)

        if os.path.isfile(full_path):
            count += 1
        elif os.path.isdir(full_path):
            count += count_files(full_path)

    return count
import os

def count_files(directory_path):
    count = 0

    for item in os.listdir(directory_path):
        full_path = os.path.join(directory_path, item)

        if os.path.isfile(full_path):
            count += 1
        elif os.path.isdir(full_path):
            count += count_files(full_path)

    return count
def find_infected_files(directory_path, extension):
    infected = []

    for item in os.listdir(directory_path):
        full_path = os.path.join(directory_path, item)

        if os.path.isfile(full_path) and item.endswith(extension):
            infected.append(full_path)

        elif os.path.isdir(full_path):
            infected.extend(find_infected_files(full_path, extension))

    return infected
finance = find_infected_files("breach_data/Finance", ".encrypted")
hr = find_infected_files("breach_data/HR", ".encrypted")
sales = find_infected_files("breach_data/Sales", ".encrypted")

print("Finance:", len(finance))
print("HR:", len(hr))
print("Sales:", len(sales))

git add .
git commit -m "Completed recursive file system analysis"
git push
