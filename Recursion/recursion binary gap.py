""" Given a positive integer n, 
find and return the longest distance between any two adjacent 1's in the binary representation of n. 
If there are no two adjacent 1's, return 0.
Two 1's are adjacent if there are only 0's separating them (possibly no 0's). 
The distance between two 1's is the absolute difference between their bit positions. 
For example, the two 1's in "1001" have a distance of 3.
"""

class Solution:
    def binaryGap(self, n: int) -> int:
        binary_representation = bin(n)[2:]  # Get the binary representation of n as a string
        last_position = -1  # Initialize the last position of '1' to -1
        max_distance = 0  # Initialize the maximum distance to 0

        for i, bit in enumerate(binary_representation):
            if bit == '1':
                if last_position != -1:  # If we have seen a '1' before
                    distance = i - last_position  # Calculate the distance from the last '1'
                    max_distance = max(max_distance, distance)  # Update max distance if needed
                last_position = i  # Update the last position of '1'

        return max_distance