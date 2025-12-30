class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size #Create an emoty list of size 7, that is our hash table 

    def _hash(self, key):
        my_hash = 0 
        for letter in key:
            #my_hash = (my_hash+ ord(letter)*23) % len(self.data_map) # Should give a number from 1-7 
            my_hash = hash(key) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, " : ", val)

    def set_item(self, key, value):
        index = self._hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = [] 
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self._hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    print("Value found")
                    return self.data_map[index][i][1]
        print("Key not found")
        return None 
    
    def keys(self): #Print all keys 
        all_keys = [] 
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0]) #Only want the key 
        return all_keys
    
    def item_in_common(self, list1, list2):
        my_dict = {} 
        for i in list1:
            my_dict[i] = True 
        for j in list2:
            if j in my_dict:
                return True 
        return False
    
    def find_duplicates(self, list1):
        my_dict = {}
        duplicates = []
        for i in list1:
            if i in my_dict:
                my_dict[i] += 1 
                if my_dict[i] == 2:
                    duplicates.append(i)
            else:
                my_dict[i] = 1

        return duplicates
    
    def first_non_repeating_character(self, s):
        freq = {}
        #Count frequency of all 
        for char in s:
            #freq[char] = freq.get(char, 0) + 1
            if char in freq:
                freq[char] += 1 
            else:
                freq[char] = 1 
        #Second pass, check for first character with frequency = 1
        for char in s:
            if(freq[char] == 1):
                return char 
    
    def group_anagrams(self, words):
        anagrams = {}
        for word in words:
            key = ''.join(sorted(word, reverse=False))
            if key in anagrams:
                anagrams[key].append(word)
            else:
                anagrams[key] = [word]
        return list(anagrams)
    
    def two_sums(self, nums, target):
        seen = {} 
        for index, num in enumerate(nums):
            complement = target - num 
            if complement in seen:
                return [seen[complement], index]
            seen[num] = index

    def subarray_sum(self, nums, k):
        prefix_count = {0:1}
        sum = 0
        count = 0

        for num in nums:
            sum += num 

            if sum - k in prefix_count:
                count = count + prefix_count[sum-k] 

            prefix_count[sum] = prefix_count.get(sum, 0) + 1 
        return count 
    
    def remove_duplicates(self, nums): #Using set
        #return list(set(nums)) #Order does not matter
        seen = set()
        result = [] 

        for num in nums:
            if num not in seen:
                seen.add(num)
                result.append(num)
        return result 
    
    def has_unique_chars(self, strs): #Determine if all characters are unique
        seen = set() 
        for char in s:
            if char in seen:
                return False 
            seen.add(char) #Opt 
        return True
    
    def find_pairs(self, nums, k): #Find pairs which result in 'k'
        seen = set()
        pairs = set() 

        for num in nums:
            complement = num - k 
            if complement in seen:
                pairs.add( (min(num, complement), max(num, complement)) )
            seen.add(num)

        return list(pairs)
    
    def longest_consecutive(self, nums): #longest sequence in sorted order
        num_set = set(nums)
        longest = 0 

        for num in num_set:
            if num-1 not in num_set: #If num is the start of a sequence
                current_num = num 
                current_streak = 1 
                
                while current_num + 1 in num_set:
                    current_num += 1 
                    current_streak += 1 

                longest = max(longest, current_streak)
        return longest




hash_table = HashTable()

hash_table.set_item("apple", 10)
hash_table.set_item("banana", 20)
hash_table.set_item("orange", 30)
hash_table.set_item("olof", 40)

hash_table.print_table()

hash_table.get_item("olof")
hash_table.get_item("hippo")

print(hash_table.keys())

list1 = [1,3,5]
list2 = [6,7,3]
print(hash_table.item_in_common(list1, list2))

list1 = [1,3,4,3,2,5,7,7,8,8,6,1]
print(hash_table.find_duplicates(list1))

s = "leetcode"
print("First no repeating charc is ",hash_table.first_non_repeating_character(s))

strs = ["eat","tea","tan","ate","nat","bat"]
print(hash_table.group_anagrams(strs))

nums = [2, 7, 11, 15]
target = 9
print(hash_table.two_sums(nums, target))

nums = [1,2,1,1,1]
k = 4
print(hash_table.subarray_sum(nums, k))