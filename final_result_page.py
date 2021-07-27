root=tk.Tk()

l1=tk.Label(text="Your done with the quiz!! congrats !!").grid(row=6,column=0)
l2=tk.Label(text="Hope you had fun!! ").grid(row=7,column=0)
l3=tk.Label(text="Here are your results: ").grid(row=8,column=0)
l4=tk.Label(text="Total marks: "+str(totalmarks)+"out of 40").grid(row=9,column=0)
l5=tk.Label(text="Thank you for playing!!").grid(row=10,column=0)
root.mainloop()
