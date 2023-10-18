class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        # Create an adjacency list to represent the graph
        graph = [[] for _ in range(n)]
        in_degree = [0] * n
        
        # Build the graph and calculate in-degrees
        for relation in relations:
            prev, next_course = relation
            graph[prev - 1].append(next_course - 1)
            in_degree[next_course - 1] += 1
        
        # Initialize a queue for topological sort
        queue = []
        
        # Find courses with no prerequisites (in-degree equals 0)
        for i in range(n):
            if in_degree[i] == 0:
                queue.append(i)
        
        # Initialize a list to store the time needed for each course
        course_time = time[:]
        
        # Perform topological sort
        while queue:
            course = queue.pop(0)
            for next_course in graph[course]:
                in_degree[next_course] -= 1
                # Calculate the time needed for next_course after completing the current course
                course_time[next_course] = max(course_time[next_course], course_time[course] + time[next_course])
                if in_degree[next_course] == 0:
                    queue.append(next_course)
        
        # The answer is the maximum time needed among all courses
        return max(course_time)