import os

files = {
    'docs/diagrams/command/commandRunnerSequence-runSku.puml': '''@startuml
!include ../style.puml

Participant "Main" as main LOGIC_COLOR
Participant ":CommandRunner" as runner LOGIC_COLOR
Participant ":ParsedCommand" as cmd LOGIC_COLOR_T1
Participant ":SKUCommandHandler" as skuHandler LOGIC_COLOR_T2

== run - SKU commands ==

main -> runner ++ : run(cmd)

runner -> cmd ++ : getCommandWord()
return commandWord

alt commandWord = "addsku"
    runner -> skuHandler ++ : handleAddSku(cmd)
    return
else commandWord = "editsku"
    runner -> skuHandler ++ : handleEditSku(cmd)
    return
else commandWord = "deletesku"
    runner -> skuHandler ++ : handleDeleteSku(cmd)
    return
else
end

return
@enduml
''',
    
    'docs/diagrams/command/commandRunnerSequence-runTask.puml': '''@startuml
!include ../style.puml

Participant "Main" as main LOGIC_COLOR
Participant ":CommandRunner" as runner LOGIC_COLOR
Participant ":ParsedCommand" as cmd LOGIC_COLOR_T1
Participant ":TaskCommandHandler" as taskHandler LOGIC_COLOR_T2

== run - Task commands ==

main -> runner ++ : run(cmd)

runner -> cmd ++ : getCommandWord()
return commandWord

alt commandWord = "addskutask"
    runner -> taskHandler ++ : handleAddSkuTask(cmd)
    return
else commandWord = "edittask"
    runner -> taskHandler ++ : handleEditTask(cmd)
    return
else commandWord = "deletetask"
    runner -> taskHandler ++ : handleDeleteTask(cmd)
    return
else commandWord = "marktask"
    runner -> taskHandler ++ : handleMarkTask(cmd)
    return
else commandWord = "unmarktask"
    runner -> taskHandler ++ : handleUnmarkTask(cmd)
    return
else commandWord = "sorttasks"
    runner -> taskHandler ++ : handleSortTask(cmd)
    return
else
end

return
@enduml
''',

    'docs/diagrams/command/commandRunnerSequence-runView.puml': '''@startuml
!include ../style.puml

Participant "Main" as main LOGIC_COLOR
Participant ":CommandRunner" as runner LOGIC_COLOR
Participant ":ParsedCommand" as cmd LOGIC_COLOR_T1
Participant ":ViewCommandHandler" as viewHandler LOGIC_COLOR_T2
Participant ":Storage" as storage STORAGE_COLOR
Participant ":ViewMap" as viewMap UI_COLOR
Participant ":Ui" as ui UI_COLOR

== run - View / Utility commands ==

main -> runner ++ : run(cmd)

runner -> cmd ++ : getCommandWord()
return commandWord

alt commandWord = "listtasks"
    runner -> viewHandler ++ : handleListTasks(cmd)
    return
else commandWord = "find"
    runner -> viewHandler ++ : handleFind(cmd)
    return
else commandWord = "status"
    runner -> viewHandler ++ : handleStatus(cmd)
    return
else commandWord = "export"
    runner -> runner ++ : handleExport()
    return
else commandWord = "help"
    runner -> ui ++ : printHelp()
    return
else commandWord = "viewmap"
    runner -> viewMap ++ : printTaskMap(skuList)
    return
else commandWord = "bye" / "exit"
    runner -> storage ++ : saveState(skuList)
    return
    runner -> ui ++ : printGoodbye()
    return
    runner -> runner : isRunning = false
else commandWord = ""
    note right : no-op
else
    runner -> ui ++ : printUnknownCommand(commandWord)
    return
end

return
@enduml
'''
}

for p, c in files.items():
    with open(p, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f"Created {p}")
