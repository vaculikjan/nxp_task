class ClockCircuitAnalyzer:
    def __init__(self, outputs, input_frequency=0, target_frequency=0):
        self.outputs = outputs
        self.input_frequency = input_frequency
        self.target_frequency = target_frequency

    def find_best_match(self, desired_frequency):
        unique_keys = self.find_unique_keys()
        closest_nums = self.find_closest_numbers(desired_frequency)
        self.print_closest_numbers(closest_nums, unique_keys)

    def find_closest_numbers(self, desired_value):
        def dfs(nested_dict, path):
            closest_nums = []
            closest_diff = float('inf')

            for key, value in nested_dict.items():
                if isinstance(value, dict):
                    sub_path = path + [key]
                    sub_nums, diff = dfs(value, sub_path)
                    if sub_nums:
                        if diff < closest_diff:
                            closest_nums = sub_nums
                            closest_diff = diff
                        elif diff == closest_diff:
                            closest_nums.extend(sub_nums)
                elif isinstance(value, list):
                    for i, num in enumerate(value):
                        if isinstance(num, dict):
                            sub_path = path + [key, i]
                            sub_nums, sub_diff = dfs(num, sub_path)
                            if sub_nums:
                                if sub_diff < closest_diff:
                                    closest_nums = sub_nums
                                    closest_diff = sub_diff
                                elif sub_diff == closest_diff:
                                    closest_nums.extend(sub_nums)
                        elif isinstance(num, float):
                            diff = abs(num - desired_value)
                            if diff < closest_diff:
                                closest_nums = [{"value": num, "path": path + [key, i]}]
                                closest_diff = diff
                            elif diff == closest_diff:
                                closest_nums.append({"value": num, "path": path + [key, i]})
            return closest_nums, closest_diff

        closest_numbers, _ = dfs(self.outputs, [])
        return closest_numbers

    def print_closest_numbers(self, closest_numbers, unique_keys):
        if closest_numbers:
            print(f"Possible configurations for input frequency {self.input_frequency} and target frequency {self.target_frequency}:")
            for i, number in enumerate(closest_numbers):
                reversed_path = self.reverse_list_by_pairs(number["path"])
                path_str = self.create_path_string(reversed_path)

                for key in unique_keys:
                    if key not in reversed_path:
                        path_str += f" -> {key} not used"

                print(f"{i} - Achieved frequency is {number['value']} with configuration: {path_str}")
        else:
            print("No numbers found in the nested dictionary.")

    @staticmethod
    def create_path_string(reversed_path):
        path_str = ""
        for i in range(0, len(reversed_path), 2):
            path_str += " input ".join(str(element) for element in reversed_path[i:i + 2])
            if i + 2 < len(reversed_path):
                path_str += " -> "
        return path_str

    def find_unique_keys(self):
        unique_keys = set()
        self._find_unique_keys(self.outputs, unique_keys)
        return unique_keys

    def _find_unique_keys(self, dictionary, unique_keys):
        for key, value in dictionary.items():
            unique_keys.add(key)
            if isinstance(value, dict):
                self._find_unique_keys(value, unique_keys)
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        self._find_unique_keys(item, unique_keys)

    @staticmethod
    def reverse_list_by_pairs(lst):
        if len(lst) % 2 != 0:
            return "The list does not have an even number of elements."
        reversed_lst = []
        for i in range(len(lst) - 1, 0, -2):
            reversed_lst.extend(lst[i - 1:i + 1])
        return reversed_lst

