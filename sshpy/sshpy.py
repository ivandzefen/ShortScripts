import paramiko
import sys
''' sshpy
    python
    usage : python3 sshpy.py 'hostname' 'username' 'password'(optional) 'port(optional)'''
def main(args) :
    client=paramiko.SSHClient()
    client.load_system_host_keys()
    connect_info={'hostname':None,
                  'username':None,
                  'password':None,
                  'port':22,
                  'allow_agent':False,
                  'look_for_keys':False}
    l=len(args)
    if l<2 :
        print('too few arguements')
        return()
    elif l>4 :
        print('too many arguements')
        return
    else :
        for i in range(l) :
            for key in connect_info:
                if connect_info[key]==None :
                    connect_info[key]=args[i]
                    break
                elif connect_info[key]==22:
                    connect_info[key]=int(args[i])
                    break
    try :
        client.connect(**connect_info)
    except Exception as ex :
        print(ex)
        return
    print('welcome to sshpy (enter exit to quit)')
    while True :
        cmd=str(input(connect_info['username']+'@'+connect_info['hostname']+':'))
        if cmd=='exit':
            client.close()
            return
        stdin, stdout, stderr=client.exec_command(cmd)
        print(stdout.read().decode("utf8")+' '+stderr.read().decode("utf8"))


if __name__=='__main__' :
    args=sys.argv[1:]
    main(args)
