from typing import Set, Tuple, List


class Generator:

    def number(self, n: int):
        raise NotImplementedError()

    def get_closest_index_for(self, num: int, index_used: Set[int] = set()) -> Tuple[int, int, bool]:
        if num < 0:
            raise ValueError('Negative numbers not supported')
        i = -1
        prev_index = 0
        seq_num = -1
        while seq_num < num:
            if i not in index_used:
                prev_index = i
                i += 1
                seq_num = self.number(i)
            else:
                i += 1

        if seq_num > num:
            return prev_index, self.number(prev_index), False
        return i, seq_num, True

    def get_sum_solution_for(self, num: int) -> Tuple[Set[int], str]:
        if num < 0:
            raise ValueError('Negative numbers not supported')

        index_used = set()
        remaining_sum = num
        while remaining_sum >= 0:
            index, partial_solution, exact = self.get_closest_index_for(remaining_sum, index_used)
            index_used.add(index)
            remaining_sum -= partial_solution
            if remaining_sum == 0:
                break
            if remaining_sum < 0:
                raise Exception(f'Can not represent {num}')

        return f'{num}=' + '+'.join([str(self.number(i)) for i in sorted(index_used)]), index_used

    def get_every_sum_solution_up_to(self, num: int) -> List[Tuple[Set[int], str]]:
        return [
            self.get_sum_solution_for(i)
            for i in range(num + 1)
        ]
