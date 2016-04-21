#-*- coding: utf-8 -*-
from slackbot.bot import Bot
from slackbot.bot import respond_to
import subprocess
import os
import shlex

def main():
    bot = Bot()
    bot.run()


@respond_to('(.*)')
def kubectl(message, kube_command):
    # slack converts double dashes into an emdash
    # so convert back before running.
    kube_command = kube_command.decode("utf-8").replace(u"\u2014", "--").encode("utf-8")
    print kube_command
    result = kubectl(kube_command)

    if not result:
        result = "There was no output from the command."

    # Wrap all replies in code blocks.
    message.reply("```{message}```".format(message=result))


def kubectl(command):
    """
    Run a kubect command and attempt to parse the results as json.
    :param command: the command to run
    """
    env = os.environ.copy()

    with open('/var/run/secrets/kubernetes.io/serviceaccount/token') as sa_token:
        token = sa_token.read()

    cmd = "/bin/kubectl {cmd} --token={token} --server={url} --insecure-skip-tls-verify=true".format(cmd=command, token=token, url=kube_api_url())


    # This will throw subprocess.CalledProcessError if the command fails.
    # Code that calls run_command should be in a try/except to handle the failure case.
    try:
        print "running command {cmd}".format(cmd=cmd)
        result = subprocess.check_output(shlex.split(cmd), env=env, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        print e.output
        return e.output

    return result


def kube_api_url():
    """
    Returns the kubernetes API url
    """
    return "https://{hostname}:{port}".format(
        hostname=os.environ['KUBERNETES_SERVICE_HOST'],
        port=os.environ['KUBERNETES_SERVICE_PORT']
    )

if __name__ == "__main__":
    main()

