from tkinter import *

from matplotlib.pyplot import text

root = Tk()
root.geometry("400x400")
root.title("Get Covid-19 Cases Data Country wise")

def showdata():
    from matplotlib import pyplot as plt
    import matplotlib.patches as mpatch
    from covid import Covid
    covid = Covid()
    cases = []
    confirmed = []
    active = []
    deaths = []
    recovered = []

    try:
        root.update()
        countries = data.get()
        country_names = countries.strip()
        country_names = country_names.replace(" ", ",")
        country_names = country_names.split(",")
        for x in country_names:
            cases.append(covid.get_status_by_country_name(x))
            root.update()
        for y in cases:
            confirmed.append(y["Confirmed"])
            active.append(y["Active"])
            recovered.append(y["Recovered"])
            deaths.append(y["Deaths"])
        confirmed_patch = mpatch.Patch(color='yellow', label='Confirmed')
        recovered_patch = mpatch.Patch(color='green', label='Recovered')
        active_patch = mpatch.Patch(color='orange', label='Active')
        deaths_patch = mpatch.Patch(color='red', label='Deaths')
        plt.legend(handles=[confirmed_patch, recovered_patch, active_patch, deaths_patch])
        for x in range(len(country_names)):
            plt.bar(country_names[x], confirmed[x], color='yellow')
            if recovered[x] > active[x]:
                plt.bar(country_names[x], recovered[x], color='green')
                plt.bar(country_names[x], active[x], color='orange')
            else:
                plt.bar(country_names[x], active[x], color='orange')
                plt.bar(country_names[x], recovered[x], color='green')
            plt.bar(country_names[x], deaths[x], color='red')
        plt.title('Current Covid Cases')
        plt.xlabel('Country Name')
        plt.ylabel('Cases(in millions)')
        plt.show()
    except Exception as e:
        print("Enter correct details")


Label(root, text="Enter all countries names\nfor whom you want get\nCovid-19 data", font="Helvetica 16 bold").pack()
Label(root, text="Enter Country name: ").pack()
data = StringVar()
data.set("Separate country names using comma or space(not both)")
entry = Entry(root, textvariable=data, width=50).pack()
Button(root, text="Get Data", command=showdata).pack()
root.mainloop()
                