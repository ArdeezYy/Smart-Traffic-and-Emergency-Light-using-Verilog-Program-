from graphviz import Digraph

def create_rtl_diagram():
    dot = Digraph(name="RTL_Architecture", format="png")
    dot.attr(rankdir="LR", compound="true", nodesep="0.6", ranksep="0.6")

    # --- INPUTS EXTERNAL ---
    with dot.subgraph(name="cluster_inputs") as inputs:
        inputs.attr(style="invis")
        inputs.node("CLK_IN", "Clk", shape="cds", style="filled", fillcolor="lightgrey")
        inputs.node("RST_IN", "reset", shape="cds", style="filled", fillcolor="lightgrey")
        inputs.node("C_IN", "C\n(Sensor)", shape="cds", style="filled", fillcolor="lightgrey")
        inputs.node("EMG_IN", "Emergency", shape="cds", style="filled", fillcolor="salmon")

    # --- MODULE MAIN ---
    with dot.subgraph(name="cluster_main") as main:
        main.attr(label="Main Module (main.v)", style="dashed", color="blue", fontcolor="blue")
        
        # --- MODULE TRAFFIC ---
        with main.subgraph(name="cluster_traffic") as traffic:
            traffic.attr(label="Traffic Module (traffic.v)", style="solid", color="black")

            # NODE TIMER
            traffic.node("TIMER", "TIMER UNIT\n(timer.v)", shape="record", style="filled", fillcolor="lightblue")
            
            # NODE FSM
            traffic.node("FSM", "FSM UNIT\n(fsm.v)", shape="record", style="filled", fillcolor="lightyellow")

            # KONEKSI INTERNAL (FSM <-> TIMER)
            traffic.edge("FSM", "TIMER", label=" ST (Start) ", color="darkgreen")
            traffic.edge("TIMER", "FSM", label=" TS, TL\n(TimeOut) ", color="darkgreen")

        # KONEKSI DARI INPUT KE DALAM TRAFFIC
        main.edge("CLK_IN", "TIMER", lhead="cluster_traffic")
        main.edge("RST_IN", "FSM", lhead="cluster_traffic")
        main.edge("C_IN", "FSM", lhead="cluster_traffic")
        
        # JALUR EMERGENCY (LANGSUNG KE FSM)
        main.edge("EMG_IN", "FSM", color="red", style="bold", label="Override")

    # --- OUTPUTS EXTERNAL ---
    with dot.subgraph(name="cluster_outputs") as outputs:
        outputs.attr(style="invis")
        outputs.node("LIGHTS_MAIN", "MAIN ROAD\n(MR, MY, MG)", shape="note", style="filled", fillcolor="lightgreen")
        outputs.node("LIGHTS_SIDE", "SIDE ROAD\n(SR, SY, SG)", shape="note", style="filled", fillcolor="lightgreen")

    # KONEKSI KELUAR
    dot.edge("FSM", "LIGHTS_MAIN")
    dot.edge("FSM", "LIGHTS_SIDE")

    return dot

if __name__ == "__main__":
    diagram = create_rtl_diagram()
    diagram.render("system_block_diagram", cleanup=True)
    print("Gambar 'system_block_diagram.png' berhasil dibuat!")