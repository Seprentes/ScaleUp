from PySide6.QtDesigner import QPyDesignerCustomWidgetCollection
from PySide6_FileSelection.FileSelection import FileSelection

TOOLTIP = "File selection widget (Python)"
DOM_XML = """
<ui language="c++">
    <widget class="FileSelection" name="fileSelection">
        <property name="geometry">
            <rect>
                <x>0</x>
                <y>0</y>
                <width>247</width>
                <height>56</height>
            </rect>
        </property>
        <property name="existingFile">
            <bool>true</bool>
        </property>
    </widget>
</ui>
"""

if __name__ == "__main__":
    QPyDesignerCustomWidgetCollection.registerCustomWidget(
        FileSelection, module="FileSelection",
        tool_tip=TOOLTIP, xml=DOM_XML
    )
