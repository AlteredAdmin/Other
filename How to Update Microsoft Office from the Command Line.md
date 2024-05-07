# How to Update Microsoft Office from the Command Line

Updating Microsoft Office without opening any Office application can be a crucial task, especially in managed IT environments or when preparing systems for deployment. This guide provides detailed steps on how to initiate updates from the command line, making the process efficient and unobtrusive to end-users.

## Triggering a Basic Update

To initiate a basic update of Microsoft Office from the command line, use the following command:

```bash
"C:\Program Files\Common Files\microsoft shared\ClickToRun\OfficeC2RClient.exe" /update user
```

This command will trigger the Office Update GUI, allowing you to follow on-screen instructions to complete the update process.

## Performing a Silent Update

If you prefer to update Office silently, without any user interaction and ensuring that applications are forcefully closed during the update, use the following command:

```bash
"C:\Program Files\Common Files\microsoft shared\ClickToRun\OfficeC2RClient.exe" /update user displaylevel=false forceappshutdown=true
```

This approach is particularly useful when updates need to be deployed without interrupting the user workflow.

## Changing the Office Update Channel

Changing the update channel can be necessary to receive updates more frequently or to ensure more stable builds depending on your requirements. To change the update channel to the Current Channel, which provides the most frequent updates, use the command below:

```bash
"C:\Program Files\Common Files\Microsoft Shared\ClickToRun\OfficeC2RClient.exe" /changesetting Channel=Current
```

To apply this setting across multiple computers in a network, consider using tools like PsExec. Here’s an example command that uses PsExec to change the update channel for a list of computers provided in a text file named `computers.txt`:

```bash
psexec @computers.txt -d -n 3 cmd /c "C:\Program Files\Common Files\Microsoft Shared\ClickToRun\OfficeC2RClient.exe" /changesetting Channel=Current
```

## Updating to a Specific Version

If a specific build of Office is needed, perhaps for compatibility reasons or to roll back to a more stable release, you can specify the exact version to update to:

```bash
“C:\Program Files\Common Files\Microsoft Shared\ClickToRun\OfficeC2RClient.exe” /update user updatetoversion=X.X.X.X
```

Replace `X.X.X.X` with the full build number you wish to install. You can find these numbers on the Microsoft Update History site.

## General Tips

- Always ensure that the path to `OfficeC2RClient.exe` is correct. It might vary slightly depending on the system architecture (x86 vs x64) or the installation path.
- Consider testing these commands in a controlled environment before widespread deployment.
- Regularly check Microsoft’s documentation for any changes to command-line options or paths after major updates or new releases of Office.

Using these commands, you can streamline the management of Office installations across an organization, ensuring that all users run the most current and secure versions of their productivity software without manual intervention.
