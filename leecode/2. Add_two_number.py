class SOlution:
    def addTwoNumber(self, l1, l2):
        res = sum = 0
        head = add = ListNode()
        while l1 or l2:
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2: 
                sum += l2.val
                l2 = l2.next
            
            tot += res

            add.val = sum % 10
            res = sum //10
            sum = 0

            if l1 or l2 or res > 0:
                add.next = ListNode()
                add = add.next
            
        if res != 0:
                add.val = res
        
        return head
