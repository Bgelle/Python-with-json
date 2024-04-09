import json
var={
    "stores":
        {
            "pharmacy":"apollo",
          "supermarket":"spar",
           "cosmetics":"lakme"
    },
    "products":
        {
            "apollo":"tablets",
            "spar":"flour",
            "lakme":"creme"

        },
    "prices":
        {
            "tablets":50,
            "flour":80,
            "creme":160
        }

}
with open("d:\samplejson2.json","w") as p:
    json.dump(var,p)
print(p)