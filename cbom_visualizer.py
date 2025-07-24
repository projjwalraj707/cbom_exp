import graphviz, json
dot = graphviz.Digraph('G', filename='abc.gv')
#dot = graphviz.Digraph('G')

cbomFileLoc = "./mastercard_cbom.json"
cbom = {}
with open(cbomFileLoc) as f:
    cbom = json.load(f)

cbomComponents = {}
for component in cbom["components"]:
    cbomComponents[component["bom-ref"]] = component # Map each component to its bom-ref for efficienet access
    # Add the nodes to the graph
    if component['cryptoProperties']['assetType'] == 'algorithm':
        dot.node(component['bom-ref'], component['name'].split('@')[0], style='filled', color='#ffd966', shape='box') # Algorithm is shown with yellow color
    elif component['cryptoProperties']['assetType'] == 'related-crypto-material':
        dot.node(component['bom-ref'], component['name'].split('@')[0], color='blue', shape='box') # assets like keys are shown with blue color
    elif component['cryptoProperties']['assetType'] == 'protocol':
        dot.node(component['bom-ref'], component['name'].split('@')[0], style='filled', color='#c9c9c9', shape='box') # Protocol is shown with grey color
    elif component['cryptoProperties']['assetType'] == 'certificate':
        dot.node(component['bom-ref'], component['name'].split('@')[0], style='filled', color='#a9d18f', shape='box') # Certificate is shown with green color
    else:
        dot.node(component['bom-ref'], component['name'].split('@')[0]) # all other assets (if any are added in the future) are shown simply using black color and elliptical shape

for dependency in cbom['dependencies']:
    toID = dependency["ref"]
    for fromID in dependency['dependsOn']:
        dot.edge(fromID, toID, label='u')
    if 'provides' in dependency:
        for fromID in dependency['provides']:
            dot.edge(fromID, toID, label='i')

dot.attr(label='\n\n\n\n\nYellow: Algorithms\nGrey: Protocols\nGreen: Certificates\nBlue: Related Crypto Material', color='yellow')
dot.view()
