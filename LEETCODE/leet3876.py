def uniformArray(nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """
        ansodd=[]
        odd=float('inf')
        anseven=[]
        for i in nums1:
            if i%2!=0 and i<odd:
                odd=i
        for i in range(len(nums1)):
            if nums1[i]%2==0:       #even-odd=odd
                if nums1[i]-odd>=1:
                    ansodd.append(nums1[i])
                anseven.append(nums1[i])
            else:                   #odd-odd=even
                if nums1[i]-odd>=1:
                    anseven.append(nums1[i])
                ansodd.append(nums1[i])
        return len(nums1)==len(ansodd) or len(nums1)==len(anseven)