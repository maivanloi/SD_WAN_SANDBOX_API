

---
    -name: cau hinh switch_1
        hosts: sw_HCM
        gather_facts: False
-tasks:
    -name: show ip
    ios_command:
        Commands:
            -sh vlan br
        register: Output

        -debug:var=Output.stdout_lines
