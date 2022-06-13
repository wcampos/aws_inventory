import boto3

client = boto3.client('lambda')

def describe_lambda():
    ld_data = client.list_functions()
    idict={}
    ilist=[]

    for ld_func in ld_data['Functions']:
        ld_name = ld_func['FunctionName']
        ld_rntm = ld_func['Runtime']
        ld_hdlr = ld_func['Handler']
        ld_mmsz = ld_func['MemorySize']
        ld_strg = ld_func['EphemeralStorage']['Size']
        ld_pktp = ld_func['PackageType']
        ld_mftm = ld_func['LastModified']
        idict.update({
            'Name': ld_name,
            'Runtime': ld_rntm,
            'Handler': ld_hdlr,
            'Memory': ld_mmsz,
            'Storage Size': ld_strg,
            'Package Type': ld_pktp,
            'Last Modified': ld_mftm
        })
        ilist.append(idict.copy())
    sortedlist = sorted(ilist, key=lambda i: i['Name'])
    return sortedlist
