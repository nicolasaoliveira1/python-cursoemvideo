def maior(*nums):
    print("Analisando valores...")
    for n in nums:
        print(n,end=" ")
    print(f"Foram informados {len(nums)} valores ao todo.")
    if len(nums) != 0: # sem esse if ocorre um erro na funçao sem parametros
        print(f"O maior valor foi {max(nums)}.")
    print("=-"*20)

maior(2,9,4,5,1)
maior(6,1)
maior() 
