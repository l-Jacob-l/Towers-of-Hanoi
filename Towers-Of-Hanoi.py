

# og = origion of the disk/ tower the disk moves from
# hlp = helper tower/ tower the disk temporarily uses to hold disks
# dest = final destination of the disks

# Recursive Function
def TowersOfHanoi(num, og, hlp, dest):
    count = 2**num - 1
    if num == 1:
        print('Disk moved from tower ' + og + ' to tower ' + dest)
        return count
    else:
        # Recursive Function call -swaps destination and helper
        TowersOfHanoi(num - 1, og, dest, hlp)
        print('Disk moved from tower ' + og + ' to tower ' + dest)

        # 2nd Recursive Function call -swaps origion and helper
        TowersOfHanoi(num - 1, hlp, og, dest )
        return count



print('It only takes ' + str(TowersOfHanoi(3, 'A', 'B', 'C')) + ' moves!')

# Steps to solve the puzzle when number of disks = 3
# 1. TowersOfHanoi(3, 'A', 'B', 'C') 
# 2. TowersOfHanoi(2, 'A', 'C', 'B') 
# 3. TowersOfHanoi(1, 'A', 'B', 'C') 
# 4. 1st disk moved from tower A to tower C
# 5. TowersOfHanoi(2, 'A', 'C', 'B') 
# 6. 2nd disk moved from tower A to tower B
# 7. TowersOfHanoi(1, 'C', 'A', 'B') 
# 8. 1st disk moved from tower C to tower B
# 9. TowersOfHanoi(3, 'A', 'B', 'C')
# 10. 3rd disk moved from tower A to tower C
# 11. TowersOfHanoi(2, 'B', 'A', 'C')
# 12. TowersOfHanoi(1, 'B', 'C', 'A')
# 13. TowersOfHanoi(1, 'B', 'A', 'C')
# 14. 1st disk moved from tower B to tower A
# 16. 2nd disk moved from tower B to tower C
# 17. TowersOfHanoi(1, 'A', 'B', 'C')
# 18. 1st disk moved from tower A to tower C
# 19. It only takes 7 moves!
