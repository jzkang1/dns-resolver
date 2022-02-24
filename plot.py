import matplotlib as mpl
import matplotlib.pyplot as plt

data = {
    "Google.com": {
        "own": [57.71803855895996, 55.490732192993164, 58.80904197692871, 54.099082946777344, 56.79202079772949, 48.34270477294922, 51.86915397644043, 61.54799461364746, 65.02342224121094, 63.58003616333008],
        "local": [4.956245422363281, 2.0225048065185547, 1.995086669921875, 1.6155242919921875, 1.310110092163086, 3.6373138427734375, 1.6644001007080078, 1.7633438110351562, 1.9979476928710938, 1.9946098327636719],
        "google": [15.043973922729492, 12.084245681762695, 4.921913146972656, 10.036230087280273, 12.921571731567383, 10.627508163452148, 13.396024703979492, 10.959625244140625, 5.410671234130859, 12.12930679321289] 
    },
    "Youtube.com": {
        "own": [54.81910705566406, 53.462982177734375, 56.8234920501709, 66.01095199584961, 52.34265327453613, 65.51122665405273, 54.49628829956055, 55.539846420288086, 55.06491661071777, 50.21309852600098],
        "local": [0.9977817535400391, 2.1834373474121094, 1.2259483337402344, 1.996755599975586, 1.0225772857666016, 3.5657882690429688, 2.9942989349365234, 2.552032470703125, 5.986213684082031, 4.814386367797852],
        "google": [13.966560363769531, 28.700590133666992, 14.322757720947266, 11.696577072143555, 12.965679168701172, 10.358572006225586, 10.21265983581543, 19.15764808654785, 10.994672775268555, 11.096954345703125]
    },
    "Facebook.com": {
        "own": [35.77280044555664, 40.343284606933594, 48.694610595703125, 47.35445976257324, 50.28486251831055, 50.27365684509277, 48.85458946228027, 49.69453811645508, 48.12002182006836, 44.92950439453125],
        "local": [1.9974708557128906, 3.9887428283691406, 3.7047863006591797, 1.0273456573486328, 3.1402111053466797, 7.587671279907227, 3.8118362426757812, 3.571748733520508, 1.0263919830322266, 3.603219985961914],
        "google": [29.211044311523438, 21.15917205810547, 11.657238006591797, 14.133214950561523, 12.883663177490234, 10.1776123046875, 15.537500381469727, 12.856721878051758, 21.34871482849121, 12.017011642456055]
    },
    "Qq.com": {
        "own": [273.00000190734863, 289.5021438598633, 279.5131206512451, 275.07758140563965, 276.16357803344727, 292.9239273071289, 276.0758399963379, 272.82166481018066, 274.6849060058594, 275.21252632141113],
        "local": [1.9936561584472656, 2.8383731842041016, 2.0246505737304688, 2.315044403076172, 1.7004013061523438, 4.195928573608398, 7.550477981567383, 2.076387405395508, 1.5492439270019531, 2.7894973754882812],
        "google": [6.978511810302734, 7.895231246948242, 7.961034774780273, 5.925893783569336, 5.600690841674805, 5.367517471313477, 5.778312683105469, 5.323886871337891, 5.742073059082031, 5.4416656494140625]
    },
    "Taobao.com": {
        "own": [109.81178283691406, 113.12365531921387, 117.14625358581543, 117.01297760009766, 107.27047920227051, 109.54570770263672, 117.50626564025879, 109.04622077941895, 106.33397102355957, 123.3375072479248],
        "local": [261.6097927093506, 271.8973159790039, 14.960050582885742, 20.030975341796875, 15.009403228759766, 13.976812362670898, 19.733428955078125, 243.32785606384277, 85.8466625213623, 79.90002632141113],
        "google": [6.098031997680664, 5.150318145751953, 4.920482635498047, 4.920244216918945, 4.949808120727539, 5.523204803466797, 5.163669586181641, 5.696535110473633, 5.391597747802734, 4.8885345458984375]
    },
    "Yahoo.com": {
        "own": [45.519113540649414, 46.280860900878906, 46.03934288024902, 57.0828914642334, 60.81223487854004, 44.17872428894043, 46.62752151489258, 55.33647537231445, 49.63421821594238, 39.69883918762207],
        "local": [10.176897048950195, 5.983829498291016, 3.9899349212646484, 3.986835479736328, 2.991199493408203, 2.8107166290283203, 3.390073776245117, 2.313375473022461, 2.292633056640625, 2.0236968994140625],
        "google": [4.989862442016602, 5.893468856811523, 5.24592399597168, 6.984710693359375, 4.952669143676758, 6.565093994140625, 6.712675094604492, 5.396127700805664, 5.928993225097656, 5.67936897277832]
    },
    "Zhihu.com": {
        "own": [277.8022289276123, 294.06070709228516, 301.97596549987793, 281.4936637878418, 278.4695625305176, 295.7301139831543, 300.3575801849365, 291.8269634246826, 297.14179039001465, 296.5888977050781],
        "local": [13.961553573608398, 14.431953430175781, 15.35344123840332, 15.371322631835938, 16.370773315429688, 15.22374153137207, 14.045238494873047, 13.706207275390625, 12.901782989501953, 14.080286026000977],
        "google": [11.095762252807617, 11.404275894165039, 14.786243438720703, 11.200189590454102, 11.558055877685547, 14.271020889282227, 12.603521347045898, 11.85464859008789, 16.36958122253418, 11.856555938720703]
    },
    "Wikipedia.org": {
        "own": [60.148000717163086, 61.76185607910156, 68.85743141174316, 98.7696647644043, 64.01872634887695, 102.52737998962402, 98.91581535339355, 62.7436637878418, 113.06333541870117, 98.86956214904785],
        "local": [1.001119613647461, 2.057790756225586, 4.372119903564453, 1.9938945770263672, 2.6934146881103516, 2.1860599517822266, 2.6950836181640625, 2.4499893188476562, 2.0704269409179688, 1.9979476928710938],
        "google": [27.663230895996094, 15.311956405639648, 12.195110321044922, 13.933420181274414, 14.61172103881836, 13.396024703979492, 11.122941970825195, 10.857343673706055, 11.00778579711914, 10.716676712036133]
    },
    "Instagram.com": {
        "own": [39.603233337402344, 38.24949264526367, 41.332244873046875, 46.77462577819824, 41.275739669799805, 38.329362869262695, 40.34852981567383, 45.563697814941406, 41.87202453613281, 44.64840888977051],
        "local": [1.9938945770263672, 1.0118484497070312, 2.289295196533203, 1.7189979553222656, 2.064228057861328, 1.9259452819824219, 1.7006397247314453, 2.062082290649414, 2.9277801513671875, 1.1293888092041016],
        "google": [16.151905059814453, 15.612602233886719, 10.412931442260742, 14.885187149047852, 20.07746696472168, 14.50204849243164, 10.042428970336914, 21.780729293823242, 14.959335327148438, 12.011289596557617]
    },
    "Netflix.com": {
        "own": [55.36603927612305, 61.62428855895996, 54.00562286376953, 63.09318542480469, 68.80354881286621, 69.06747817993164, 70.21856307983398, 103.70254516601562, 64.39018249511719, 55.855751037597656],
        "local": [2.0232200622558594, 2.0334720611572266, 2.2056102752685547, 2.0363330841064453, 2.9947757720947266, 2.992391586303711, 1.9946098327636719, 1.9946098327636719, 2.0287036895751953, 2.539396286010742],
        "google": [27.997732162475586, 12.965917587280273, 20.089149475097656, 52.42633819580078, 92.14949607849121, 26.087522506713867, 18.04971694946289, 13.497591018676758, 11.756658554077148, 13.227224349975586]
    },
}

mpl.use('agg')
resolvers = ["own", "local", "google"]

fig = plt.figure(figsize =(20, 12))
ax = fig.add_subplot(111)
box_data = []

for domain in data:
    site_data = []
    for resolver in resolvers:
        box_data.append(data[domain][resolver])
bp = ax.boxplot(box_data)

# colors = ['lightred', 'lightblue', 'lightgreen']
# for patch, color in zip(bp['boxes'], colors*10):
#     patch.set_facecolor(color)

plt.title("Dns Resolution Times")
plt.ylabel("Time to resolve (ms)")

plt.xticks(rotation=90)
xlabels = []
for i in data:
    for resolver in resolvers:
        xlabels.append(i + "\n" + resolver + " DNS")

ax.set_xticklabels(xlabels)

fig.savefig("plot.png", bbox_inches = 'tight')