/***************************************************************************************
* Copyright (c) 2023 Yusong Yan, Beijing 101 High School
* Copyright (c) 2023 Yusong Yan, University of Washington - Seattle
*
* YSYX-NPC is licensed under Mulan PSL v2.
* You can use this software according to the terms and conditions of the Mulan PSL v2.
* You may obtain a copy of Mulan PSL v2 at:
*          http://license.coscl.org.cn/MulanPSL2
*
* THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND,
* EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT,
* MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.
*
* See the Mulan PSL v2 for more details.
***************************************************************************************/

package npc.axi

class AXIArbiter extends Module{
    // Rule: LSU Read > IFU iFetch
    // This is the interface between the "module parts external" to "SoC/simulation external"

    val IFU_AR = IO(new Flipped(AXIMasterAR))
    val IFU_R  = IO(new Flipped(AXIMasterR))
    val LSU_AR = IO(new Flipped(AXIMasterAR))
    val LSU_R  = IO(new Flipped(AXIMasterR))

    val ArbitAR = IO(new AXIMasterAR)
    val ArbitR  = IO(new AXIMasterR)

    if(IFU_AR.oMasterARvalid.asBool && LSU_AR.oMasterARvalid.asBool){
        // Both LSU and IFU send read request, satisfy LSU first
        LSU_AR <> ArbitAR
        LSU_R  <> ArbitR
    }else if(IFU_AR.oMasterARvalid.asBool && (!LSU_AR.oMasterARvalid.asBool)){
        // Only IFU
        IFU_AR <> ArbitAR
        IFU_R  <> ArbitR
    }else if((!IFU_AR.oMasterARvalid.asBool) && LSU_AR.oMasterARvalid.asBool){
        // Only LSU
        LSU_AR <> ArbitAR
        LSU_R  <> ArbitR
    }else{
        // No read request
        ArbitAR.oMasterARvalid := false.B
        ArbitR.oMasterRready   := false.B
    }
}