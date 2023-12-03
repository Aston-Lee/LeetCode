class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        def add_interval(intervals, new_interval):
            """
            Adds a new interval to the set of intervals, merging with existing intervals if necessary.
            Returns the total length of the new interval that does not overlap with existing intervals.
            """
            start, end = new_interval
            new_area = end - start

            # Remove overlapping intervals and calculate the non-overlapping area
            to_remove = set()
            for interval in intervals:
                if interval[1] < start or interval[0] > end:
                    continue
                to_remove.add(interval)
                # Adjust the new area by subtracting the overlapping parts
                new_area -= min(end, interval[1]) - max(start, interval[0])

            # Remove overlapping intervals
            for interval in to_remove:
                intervals.remove(interval)
                # Extend the new interval to include the removed one
                start = min(start, interval[0])
                end = max(end, interval[1])

            # Add the merged new interval
            intervals.add((start, end))

            return new_area

        # Initialize the set of intervals and the worklog
        painted_intervals = set()
        worklog = []

        # Process each painting interval
        for interval in paint:
            new_area = add_interval(painted_intervals, interval)
            worklog.append(new_area)

        return worklog