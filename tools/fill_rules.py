# UI colour assignments for every VS Code theme key the Sweet C base did not set.
# Values are role references resolved per flavour:
#   'role' / 'role@AA'          UI role (+ hex alpha)
#   'syn:role' / 'syn:role@AA'  syntax role
#   'none'                      fully transparent
import re

N = 'none'

EXPLICIT = {
    # ---- global / contrast (transparent: we never want HC outlines in a dark theme)
    'contrastActiveBorder': N, 'contrastBorder': N,
    'disabledForeground': 'fgFaint', 'widget.border': 'border',
    'window.activeBorder': 'border', 'window.inactiveBorder': 'border',
    'surface.background': 'bgWidget', 'surface.foreground': 'fg', 'surface.border': 'border',
    'editor.border': N,
    'textBlockQuote.background': 'bgWidget', 'textBlockQuote.border': 'accent@80',
    'textPreformat.foreground': 'syn:number', 'textPreformat.background': 'bgWidget', 'textPreformat.border': N,
    'textSeparator.foreground': 'border',
    'toolbar.hoverOutline': N, 'toolbar.activeBackground': 'accent@33',
    'editorActionList.background': 'bgWidget', 'editorActionList.foreground': 'fg',
    'editorActionList.focusForeground': 'fg', 'editorActionList.focusBackground': 'accent@38',
    # ---- buttons / inputs
    'button.border': N, 'button.separator': 'white@40', 'button.secondaryHoverBackground': 'bgHover2', 'button.secondaryBorder': N,
    'checkbox.foreground': 'fg', 'checkbox.disabled.background': 'bgHover', 'checkbox.disabled.foreground': 'fgFaint',
    'checkbox.selectBackground': 'bgWidget', 'checkbox.selectBorder': 'accent',
    'radio.activeForeground': 'fg', 'radio.activeBackground': 'accent@40', 'radio.activeBorder': 'accent',
    'radio.inactiveForeground': 'fgMuted', 'radio.inactiveBackground': N, 'radio.inactiveBorder': 'border', 'radio.inactiveHoverBackground': 'bgHover',
    'dropdown.listBackground': 'bgWidget',
    'inputOption.activeForeground': 'fg', 'inputOption.hoverBackground': 'bgHover2',
    'inputValidation.errorForeground': 'fg', 'inputValidation.infoBackground': 'infoBg', 'inputValidation.infoForeground': 'fg',
    'inputValidation.infoBorder': 'blue', 'inputValidation.warningForeground': 'fg',
    'scrollbar.background': N,
    # ---- lists / trees
    'list.activeSelectionIconForeground': 'fg', 'list.dropBackground': 'accent@26', 'list.focusForeground': 'fg',
    'list.focusHighlightForeground': 'accent', 'list.focusOutline': N, 'list.focusAndSelectionOutline': N,
    'list.hoverForeground': 'fg', 'list.inactiveSelectionForeground': 'fg', 'list.inactiveSelectionIconForeground': 'fg',
    'list.inactiveFocusBackground': 'accent@14', 'list.inactiveFocusOutline': N, 'list.invalidItemForeground': 'red',
    'listFilterWidget.background': 'bgWidget', 'listFilterWidget.outline': 'accent@80', 'listFilterWidget.noMatchesOutline': 'red',
    'listFilterWidget.shadow': 'black@66', 'list.filterMatchBackground': 'warm@29', 'list.filterMatchBorder': N,
    'list.deemphasizedForeground': 'fgFaint', 'list.dropBetweenBackground': 'accent',
    'tree.inactiveIndentGuidesStroke': 'indent', 'tree.tableColumnsBorder': 'border', 'tree.tableOddRowsBackground': 'fg@05',
    # ---- activity bar / side bar
    'activityBar.dropBorder': 'accent', 'activityBar.activeBackground': N, 'activityBar.activeFocusBorder': 'accent',
    'activityBarTop.foreground': 'fg', 'activityBarTop.activeBorder': 'accent', 'activityBarTop.inactiveForeground': 'iconInactive',
    'activityBarTop.dropBorder': 'accent', 'activityBarTop.background': N, 'activityBarTop.activeBackground': N,
    'activityWarningBadge.foreground': 'bgDark', 'activityWarningBadge.background': 'warm',
    'activityErrorBadge.foreground': 'bgDark', 'activityErrorBadge.background': 'red',
    'profileBadge.background': 'badge', 'profileBadge.foreground': 'fg', 'profiles.sashBorder': 'border',
    'sideBar.dropBackground': 'accent@1F', 'sideBarActivityBarTop.border': 'border', 'sideBarTitle.background': 'bgDark', 'sideBarTitle.border': N,
    'sideBarStickyScroll.background': 'bgDark', 'sideBarStickyScroll.border': 'border', 'sideBarStickyScroll.shadow': 'black@66',
    # ---- minimap
    'minimap.selectionOccurrenceHighlight': 'accent@59', 'minimap.foregroundOpacity': 'black@E6', 'minimap.infoHighlight': 'blue',
    'minimap.chatEditHighlight': 'accent@80', 'minimapSlider.activeBackground': 'fgFaint@73', 'editorMinimap.inlineChatInserted': 'green@4C',
    # ---- editor groups / tabs
    'editorGroup.dropBackground': 'accent@1F', 'editorGroupHeader.noTabsBackground': 'bg', 'editorGroupHeader.border': N,
    'editorGroup.emptyBackground': 'bg', 'editorGroup.focusedEmptyBorder': N, 'editorGroup.dropIntoPromptForeground': 'fg',
    'editorGroup.dropIntoPromptBackground': 'bgWidget', 'editorGroup.dropIntoPromptBorder': 'border',
    'tab.unfocusedActiveBackground': 'bg', 'tab.activeBorder': N, 'tab.selectedBorderTop': 'accent', 'tab.selectedBackground': 'bg',
    'tab.selectedForeground': 'fg', 'tab.dragAndDropBorder': 'accent', 'tab.unfocusedActiveBorder': N,
    'tab.unfocusedInactiveBackground': 'bgDark', 'tab.unfocusedInactiveForeground': 'fgFaint', 'tab.unfocusedHoverBackground': 'bgHover',
    'tab.hoverForeground': 'fg', 'tab.unfocusedHoverForeground': 'fgMuted', 'tab.hoverBorder': N, 'tab.unfocusedHoverBorder': N,
    'tab.activeModifiedBorder': 'warm', 'tab.inactiveModifiedBorder': 'warm@80', 'tab.unfocusedActiveModifiedBorder': 'warm@80',
    'tab.unfocusedInactiveModifiedBorder': 'warm@40',
    'editorPane.background': 'bg', 'sideBySideEditor.horizontalBorder': 'border', 'sideBySideEditor.verticalBorder': 'border',
    # ---- editor core
    'editorLineNumber.dimmedForeground': 'whitespace', 'editorCursor.background': 'bg',
    'editorMultiCursor.primary.foreground': 'coral', 'editorMultiCursor.primary.background': 'bg',
    'editorMultiCursor.secondary.foreground': 'accent', 'editorMultiCursor.secondary.background': 'bg',
    'editor.placeholder.foreground': 'fgFaint', 'editor.compositionBorder': 'fg', 'editor.selectionForeground': 'fg',
    'editor.selectionHighlightBorder': N, 'editor.wordHighlightBorder': N, 'editor.wordHighlightStrongBorder': N,
    'editor.wordHighlightTextBackground': 'accent@1F', 'editor.wordHighlightTextBorder': N,
    'editor.findMatchForeground': 'fg', 'editor.findMatchHighlightForeground': 'fg',
    'editor.findMatchBorder': 'warm', 'editor.findMatchHighlightBorder': N, 'editor.findRangeHighlightBorder': N,
    'search.resultsInfoForeground': 'fgMuted', 'searchEditor.findMatchBackground': 'warm@29', 'searchEditor.findMatchBorder': N,
    'searchEditor.textInputBorder': 'border',
    'editor.inactiveLineHighlightBackground': 'bgHover', 'editorUnicodeHighlight.border': 'warm', 'editorUnicodeHighlight.background': 'warm@14',
    'editor.rangeHighlightBorder': N, 'editor.symbolHighlightBackground': 'warm@29', 'editor.symbolHighlightBorder': N,
    'editorIndentGuide.background': 'indent', 'editorIndentGuide.activeBackground': 'indentActive',
    'editorInlayHint.typeBackground': 'accent@14', 'editorInlayHint.parameterBackground': 'accent@14',
    'editor.linkedEditingBackground': 'coral@1F',
    'editorLightBulb.foreground': 'warm', 'editorLightBulbAutoFix.foreground': 'blue', 'editorLightBulbAi.foreground': 'accent',
    'editorBracketMatch.foreground': 'fg',
    'editor.foldBackground': 'accent@0F', 'editor.foldPlaceholderForeground': 'fgMuted',
    'editorOverviewRuler.background': N, 'editorOverviewRuler.findMatchForeground': 'warm@B2',
    'editorOverviewRuler.rangeHighlightForeground': 'accent@80', 'editorOverviewRuler.selectionHighlightForeground': 'accent@99',
    'editorOverviewRuler.wordHighlightForeground': 'accent@80', 'editorOverviewRuler.wordHighlightStrongForeground': 'coral@99',
    'editorOverviewRuler.wordHighlightTextForeground': 'accent@66', 'editorOverviewRuler.bracketMatchForeground': 'warm@99',
    'editorOverviewRuler.inlineChatInserted': 'green@99', 'editorOverviewRuler.inlineChatRemoved': 'red@99',
    'editorOverviewRuler.commentDraftForeground': 'fgMuted',
    'editorError.border': N, 'editorError.background': N, 'editorWarning.border': N, 'editorWarning.background': N,
    'editorInfo.border': N, 'editorInfo.background': N, 'editorHint.border': N,
    'editorUnnecessaryCode.border': N, 'editorUnnecessaryCode.opacity': 'black@99',
    'editorGutter.background': 'bg', 'editorGutter.modifiedSecondaryBackground': 'blue@80',
    'editorGutter.addedSecondaryBackground': 'green@80', 'editorGutter.deletedSecondaryBackground': 'red@80',
    'editorGutter.commentRangeForeground': 'border', 'editorGutter.commentGlyphForeground': 'fgMuted',
    'editorGutter.commentUnresolvedGlyphForeground': 'warm', 'editorGutter.foldingControlForeground': 'fgMuted',
    'editorGutter.itemGlyphForeground': 'fgMuted', 'editorGutter.itemBackground': 'bgWidget', 'editorGutter.commentDraftGlyphForeground': 'fgFaint',
    'editorCommentsWidget.resolvedBorder': 'fgFaint', 'editorCommentsWidget.unresolvedBorder': 'accent',
    'editorCommentsWidget.rangeBackground': 'accent@14', 'editorCommentsWidget.rangeActiveBackground': 'accent@26',
    'editorCommentsWidget.replyInputBackground': 'bgWidget',
    # ---- inline edit / diff / merge
    'inlineEdit.gutterIndicator.primaryBorder': 'accent', 'inlineEdit.gutterIndicator.primaryForeground': 'bgDark',
    'inlineEdit.gutterIndicator.primaryBackground': 'accent', 'inlineEdit.gutterIndicator.secondaryBorder': 'border',
    'inlineEdit.gutterIndicator.secondaryForeground': 'fg', 'inlineEdit.gutterIndicator.secondaryBackground': 'bgWidget',
    'inlineEdit.gutterIndicator.successfulBorder': 'green', 'inlineEdit.gutterIndicator.successfulForeground': 'bgDark',
    'inlineEdit.gutterIndicator.successfulBackground': 'green', 'inlineEdit.gutterIndicator.background': 'bgWidget',
    'inlineEdit.originalBackground': 'red@14', 'inlineEdit.modifiedBackground': 'green@14',
    'inlineEdit.originalChangedLineBackground': 'red@17', 'inlineEdit.originalChangedTextBackground': 'red@29',
    'inlineEdit.modifiedChangedLineBackground': 'green@14', 'inlineEdit.modifiedChangedTextBackground': 'green@29',
    'inlineEdit.originalBorder': 'red@59', 'inlineEdit.modifiedBorder': 'green@59',
    'inlineEdit.tabWillAcceptModifiedBorder': 'green', 'inlineEdit.tabWillAcceptOriginalBorder': 'red',
    'diffEditor.insertedTextBorder': N, 'diffEditor.removedTextBorder': N, 'diffEditor.border': 'border',
    'diffEditor.diagonalFill': 'border@99', 'diffEditorGutter.insertedLineBackground': 'green@24',
    'diffEditorGutter.removedLineBackground': 'red@24', 'diffEditorOverview.insertedForeground': 'green@99',
    'diffEditorOverview.removedForeground': 'red@99', 'diffEditor.unchangedRegionBackground': 'bgDark',
    'diffEditor.unchangedRegionForeground': 'fgMuted', 'diffEditor.unchangedRegionShadow': 'black@66',
    'diffEditor.unchangedCodeBackground': 'fg@08', 'diffEditor.move.border': 'fgFaint@99', 'diffEditor.moveActive.border': 'warm',
    'multiDiffEditor.headerBackground': 'bgDark', 'multiDiffEditor.background': 'bg', 'multiDiffEditor.border': 'border',
    'merge.currentHeaderBackground': 'green@4C', 'merge.currentContentBackground': 'green@1F',
    'merge.incomingHeaderBackground': 'blue@4C', 'merge.incomingContentBackground': 'blue@1F',
    'merge.border': N, 'merge.commonContentBackground': 'fg@0F', 'merge.commonHeaderBackground': 'fg@26',
    'editorOverviewRuler.currentContentForeground': 'green@B2', 'editorOverviewRuler.incomingContentForeground': 'blue@B2',
    'editorOverviewRuler.commonContentForeground': 'fgMuted@B2', 'editorOverviewRuler.commentForeground': 'fgMuted',
    'editorOverviewRuler.commentUnresolvedForeground': 'warm',
    'mergeEditor.change.background': 'blue@1F', 'mergeEditor.change.word.background': 'blue@40',
    'mergeEditor.conflict.unhandledUnfocused.border': 'warm@99', 'mergeEditor.conflict.unhandledFocused.border': 'warm',
    'mergeEditor.conflict.handledUnfocused.border': 'green@66', 'mergeEditor.conflict.handledFocused.border': 'green',
    'mergeEditor.conflict.handled.minimapOverViewRuler': 'green@B2', 'mergeEditor.conflict.unhandled.minimapOverViewRuler': 'warm@B2',
    'mergeEditor.conflictingLines.background': 'warm@1F', 'mergeEditor.changeBase.background': 'red@1F',
    'mergeEditor.changeBase.word.background': 'red@40', 'mergeEditor.conflict.input1.background': 'green@26',
    'mergeEditor.conflict.input2.background': 'blue@26',
    # ---- widgets
    'editorWidget.foreground': 'fg', 'editorWidget.resizeBorder': 'accent',
    'editorSuggestWidget.foreground': 'fg', 'editorSuggestWidget.focusHighlightForeground': 'accent',
    'editorSuggestWidget.selectedForeground': 'fg', 'editorSuggestWidget.selectedIconForeground': 'fg',
    'editorSuggestWidgetStatus.foreground': 'fgMuted',
    'editorHoverWidget.foreground': 'fg', 'editorHoverWidget.highlightForeground': 'accent', 'editorHoverWidget.statusBarBackground': 'bgDark',
    'editorGhostText.border': N, 'editorGhostText.background': N, 'editorGhostText.foreground': 'fgFaint',
    'editorStickyScroll.background': 'bg', 'editorStickyScroll.border': 'border', 'editorStickyScroll.shadow': 'black@66',
    'editorStickyScrollGutter.background': 'bg', 'editorStickyScrollHover.background': 'bgHover',
    'debugExceptionWidget.background': 'errBg', 'debugExceptionWidget.border': 'red',
    'editorMarkerNavigation.background': 'bgWidget', 'editorMarkerNavigationError.background': 'red',
    'editorMarkerNavigationWarning.background': 'warm', 'editorMarkerNavigationInfo.background': 'blue',
    'editorMarkerNavigationError.headerBackground': 'red@1F', 'editorMarkerNavigationWarning.headerBackground': 'warm@1F',
    'editorMarkerNavigationInfo.headerBackground': 'blue@1F',
    'peekViewEditorGutter.background': 'bgDark', 'peekViewEditor.matchHighlightBorder': N,
    'peekViewResult.fileForeground': 'fg', 'peekViewResult.lineForeground': 'fgMuted', 'peekViewResult.selectionForeground': 'fg',
    'peekViewTitleDescription.foreground': 'fgMuted', 'peekViewEditorStickyScroll.background': 'bgDark',
    'peekViewEditorStickyScrollGutter.background': 'bgDark',
    # ---- panel / status / menus
    'panel.dropBorder': 'accent', 'panelTitle.border': N, 'panelTitleBadge.background': 'badge', 'panelTitleBadge.foreground': 'fg',
    'panelInput.border': 'border', 'panelSection.border': 'border', 'panelSection.dropBackground': 'accent@1F',
    'panelSectionHeader.background': 'bgDark', 'panelSectionHeader.foreground': 'fgMuted', 'panelSectionHeader.border': 'border',
    'panelStickyScroll.background': 'bgDark', 'panelStickyScroll.border': 'border', 'panelStickyScroll.shadow': 'black@66',
    'outputView.background': 'bgDark', 'outputViewStickyScroll.background': 'bgDark',
    'statusBar.debuggingBorder': N, 'statusBar.noFolderForeground': 'fgUi', 'statusBar.noFolderBorder': N,
    'statusBarItem.activeBackground': 'fg@26', 'statusBarItem.hoverForeground': 'fg',
    'statusBarItem.prominentForeground': 'fg', 'statusBarItem.prominentBackground': 'badge',
    'statusBarItem.prominentHoverForeground': 'fg', 'statusBarItem.prominentHoverBackground': 'button',
    'statusBarItem.remoteHoverBackground': 'button', 'statusBarItem.remoteHoverForeground': 'fg',
    'statusBarItem.errorBackground': 'errBg2', 'statusBarItem.errorForeground': 'fg',
    'statusBarItem.errorHoverBackground': 'red@59', 'statusBarItem.errorHoverForeground': 'fg',
    'statusBarItem.warningBackground': 'warnBg2', 'statusBarItem.warningForeground': 'fg',
    'statusBarItem.warningHoverBackground': 'warm@59', 'statusBarItem.warningHoverForeground': 'fg',
    'statusBarItem.compactHoverBackground': 'fg@1F', 'statusBarItem.focusBorder': 'accent', 'statusBar.focusBorder': 'accent',
    'statusBarItem.offlineBackground': 'debugBg', 'statusBarItem.offlineForeground': 'fg',
    'statusBarItem.offlineHoverForeground': 'fg', 'statusBarItem.offlineHoverBackground': 'warm@59',
    'menubar.selectionForeground': 'fg', 'menubar.selectionBackground': 'fg@1A', 'menubar.selectionBorder': N,
    'menu.selectionBorder': N, 'menu.border': 'border',
    'commandCenter.foreground': 'fgUi', 'commandCenter.activeForeground': 'fg', 'commandCenter.background': 'bgWidget',
    'commandCenter.activeBackground': 'bgHover2', 'commandCenter.border': 'border', 'commandCenter.inactiveForeground': 'fgFaint',
    'commandCenter.inactiveBorder': 'border@80', 'commandCenter.activeBorder': 'accent@80', 'commandCenter.debuggingBackground': 'debugBg@80',
    'notificationCenter.border': 'border', 'notificationCenterHeader.foreground': 'fg', 'notificationToast.border': 'border',
    'notifications.foreground': 'fg', 'notificationLink.foreground': 'cyan', 'notificationsErrorIcon.foreground': 'red',
    'notificationsWarningIcon.foreground': 'warm', 'notificationsInfoIcon.foreground': 'blue',
    'banner.background': 'badge', 'banner.foreground': 'fg', 'banner.iconForeground': 'accent',
    'extensionButton.prominentForeground': 'white', 'extensionButton.prominentBackground': 'button',
    'extensionButton.prominentHoverBackground': 'buttonHover', 'extensionButton.background': 'button',
    'extensionButton.foreground': 'white', 'extensionButton.hoverBackground': 'buttonHover', 'extensionButton.separator': 'white@40',
    'extensionButton.border': N, 'extensionBadge.remoteBackground': 'badge', 'extensionBadge.remoteForeground': 'fg',
    'extensionIcon.starForeground': 'warm', 'extensionIcon.verifiedForeground': 'accent', 'extensionIcon.preReleaseForeground': 'coral',
    'extensionIcon.sponsorForeground': 'syn:macro', 'extensionIcon.privateForeground': 'fgMuted', 'mcpIcon.starForeground': 'warm',
    'quickInput.foreground': 'fg', 'quickInputList.focusForeground': 'fg', 'quickInputList.focusIconForeground': 'fg',
    'quickInputTitle.background': 'bgDark',
    'keybindingLabel.background': 'bgHover2', 'keybindingLabel.foreground': 'fg', 'keybindingLabel.border': 'border',
    'keybindingLabel.bottomBorder': 'border', 'keybindingTable.headerBackground': 'bgWidget', 'keybindingTable.rowsBackground': 'fg@05',
    # ---- terminal
    'terminal.border': 'border', 'terminal.selectionForeground': 'fg', 'terminal.inactiveSelectionBackground': 'accent@26',
    'terminal.findMatchBackground': 'warm@59', 'terminal.findMatchBorder': N, 'terminal.findMatchHighlightBackground': 'warm@29',
    'terminal.findMatchHighlightBorder': N, 'terminal.hoverHighlightBackground': 'accent@1F', 'terminalCursor.background': 'bgDark',
    'terminal.dropBackground': 'accent@1F', 'terminal.tab.activeBorder': 'accent',
    'terminalCommandDecoration.defaultBackground': 'fgFaint', 'terminalCommandDecoration.successBackground': 'green',
    'terminalCommandDecoration.errorBackground': 'red', 'terminalOverviewRuler.cursorForeground': 'coral@B2',
    'terminalOverviewRuler.findMatchForeground': 'warm@B2', 'terminalStickyScroll.background': 'bgDark',
    'terminalStickyScroll.border': 'border', 'terminalStickyScrollHover.background': 'bgHover',
    'terminal.initialHintForeground': 'fgFaint', 'terminalOverviewRuler.border': N, 'terminalCommandGuide.foreground': 'border',
    # ---- debug
    'debugToolBar.border': N, 'editor.inlineValuesForeground': 'fgMuted', 'editor.inlineValuesBackground': 'accent@14',
    'debugView.exceptionLabelForeground': 'fg', 'debugView.exceptionLabelBackground': 'errBg2',
    'debugView.stateLabelForeground': 'fg', 'debugView.stateLabelBackground': 'badge', 'debugView.valueChangedHighlight': 'warm',
    'debugTokenExpression.name': 'syn:member', 'debugTokenExpression.value': 'fg', 'debugTokenExpression.string': 'syn:string',
    'debugTokenExpression.boolean': 'syn:number', 'debugTokenExpression.number': 'syn:number',
    'debugTokenExpression.error': 'red', 'debugTokenExpression.type': 'syn:composite',
    'debugIcon.breakpointDisabledForeground': 'fgFaint', 'debugIcon.breakpointUnverifiedForeground': 'fgMuted',
    'debugIcon.breakpointCurrentStackframeForeground': 'warm', 'debugIcon.breakpointStackframeForeground': 'green',
    'debugIcon.startForeground': 'green', 'debugIcon.pauseForeground': 'blue', 'debugIcon.stopForeground': 'red',
    'debugIcon.disconnectForeground': 'red', 'debugIcon.restartForeground': 'green', 'debugIcon.stepOverForeground': 'blue',
    'debugIcon.stepIntoForeground': 'blue', 'debugIcon.stepOutForeground': 'blue', 'debugIcon.continueForeground': 'blue',
    'debugIcon.stepBackForeground': 'blue',
    'debugConsole.infoForeground': 'blue', 'debugConsole.warningForeground': 'warm', 'debugConsole.errorForeground': 'red',
    'debugConsole.sourceForeground': 'fgMuted', 'debugConsoleInputIcon.foreground': 'accent',
    # ---- testing
    'testing.runAction': 'green', 'testing.iconErrored': 'red', 'testing.iconFailed': 'red', 'testing.iconPassed': 'green',
    'testing.iconQueued': 'warm', 'testing.iconUnset': 'fgFaint', 'testing.iconSkipped': 'fgFaint',
    'testing.iconErrored.retired': 'red@80', 'testing.iconFailed.retired': 'red@80', 'testing.iconPassed.retired': 'green@80',
    'testing.iconQueued.retired': 'warm@80', 'testing.iconUnset.retired': 'fgFaint@80', 'testing.iconSkipped.retired': 'fgFaint@80',
    'testing.peekBorder': 'red', 'testing.peekHeaderBackground': 'red@1F', 'testing.message.error.lineBackground': 'red@17',
    'testing.message.info.decorationForeground': 'fgMuted', 'testing.message.info.lineBackground': 'blue@14',
    'testing.messagePeekBorder': 'blue', 'testing.messagePeekHeaderBackground': 'blue@1F',
    'testing.coveredBackground': 'green@14', 'testing.coveredBorder': 'green@40', 'testing.coveredGutterBackground': 'green@80',
    'testing.uncoveredBranchBackground': 'red@40', 'testing.uncoveredBackground': 'red@14', 'testing.uncoveredBorder': 'red@40',
    'testing.uncoveredGutterBackground': 'red@80', 'testing.coverCountBadgeBackground': 'badge', 'testing.coverCountBadgeForeground': 'fg',
    'testing.message.error.badgeBackground': 'red', 'testing.message.error.badgeBorder': 'red', 'testing.message.error.badgeForeground': 'bgDark',
    # ---- welcome / git / scm graph
    'welcomePage.background': 'bg', 'welcomePage.progress.background': 'bgWidget', 'welcomePage.progress.foreground': 'accent',
    'welcomePage.tileBackground': 'bgWidget', 'welcomePage.tileHoverBackground': 'bgHover2', 'welcomePage.tileBorder': 'border',
    'walkThrough.embeddedEditorBackground': 'bgDark', 'walkthrough.stepTitle.foreground': 'fg',
    'gitDecoration.renamedResourceForeground': 'cyan', 'gitDecoration.stageModifiedResourceForeground': 'blue',
    'gitDecoration.stageDeletedResourceForeground': 'red', 'gitDecoration.submoduleResourceForeground': 'syn:directive',
    'git.blame.editorDecorationForeground': 'fgFaint',
    'scmGraph.historyItemHoverLabelForeground': 'bgDark', 'scmGraph.foreground1': 'br1', 'scmGraph.foreground2': 'br2',
    'scmGraph.foreground3': 'br3', 'scmGraph.foreground4': 'br4', 'scmGraph.foreground5': 'br5',
    'scmGraph.historyItemHoverAdditionsForeground': 'green', 'scmGraph.historyItemHoverDeletionsForeground': 'red',
    'scmGraph.historyItemRefColor': 'accent', 'scmGraph.historyItemRemoteRefColor': 'cyan', 'scmGraph.historyItemBaseRefColor': 'warm',
    'scmGraph.historyItemHoverDefaultLabelForeground': 'fg', 'scmGraph.historyItemHoverDefaultLabelBackground': 'badge',
    # ---- settings editor
    'settings.modifiedItemIndicator': 'accent', 'settings.dropdownBackground': 'bgWidget', 'settings.dropdownForeground': 'fg',
    'settings.dropdownBorder': 'border', 'settings.dropdownListBorder': 'border', 'settings.checkboxBackground': 'bgWidget',
    'settings.checkboxForeground': 'fg', 'settings.checkboxBorder': 'border', 'settings.rowHoverBackground': 'fg@08',
    'settings.textInputBackground': 'bgWidget', 'settings.textInputForeground': 'fg', 'settings.textInputBorder': 'border',
    'settings.numberInputBackground': 'bgWidget', 'settings.numberInputForeground': 'fg', 'settings.numberInputBorder': 'border',
    'settings.focusedRowBackground': 'accent@14', 'settings.focusedRowBorder': N, 'settings.headerBorder': 'border',
    'settings.sashBorder': 'border', 'settings.settingsHeaderHoverForeground': 'fg',
    'breadcrumb.background': 'bg',
    'editor.snippetTabstopHighlightBorder': N, 'editor.snippetFinalTabstopHighlightBackground': N,
    'editor.snippetFinalTabstopHighlightBorder': 'accent@80',
    # ---- notebooks
    'notebook.editorBackground': 'bg', 'notebook.cellBorderColor': 'border', 'notebook.cellHoverBackground': 'bgHover',
    'notebook.cellInsertionIndicator': 'accent', 'notebook.cellStatusBarItemHoverBackground': 'fg@14',
    'notebook.cellToolbarSeparator': 'border', 'notebook.cellEditorBackground': 'bgDark', 'notebook.focusedCellBackground': 'bgHover',
    'notebook.focusedCellBorder': 'accent@80', 'notebook.focusedEditorBorder': 'accent@80', 'notebook.inactiveFocusedCellBorder': 'border',
    'notebook.inactiveSelectedCellBorder': 'border', 'notebook.outputContainerBackgroundColor': 'bgDark',
    'notebook.outputContainerBorderColor': 'border', 'notebook.selectedCellBackground': 'accent@0F', 'notebook.selectedCellBorder': 'border',
    'notebook.symbolHighlightBackground': 'accent@1F', 'notebookScrollbarSlider.activeBackground': 'fgFaint@73',
    'notebookScrollbarSlider.background': 'fgFaint@26', 'notebookScrollbarSlider.hoverBackground': 'fgFaint@40',
    'notebookStatusErrorIcon.foreground': 'red', 'notebookStatusRunningIcon.foreground': 'blue',
    'notebookStatusSuccessIcon.foreground': 'green', 'notebookEditorOverviewRuler.runningCellForeground': 'blue',
    # ---- charts / misc
    'charts.foreground': 'fg', 'charts.lines': 'border', 'charts.red': 'red', 'charts.blue': 'blue', 'charts.yellow': 'yellow',
    'charts.orange': 'warm', 'charts.green': 'green', 'charts.purple': 'accent',
    'chart.line': 'accent', 'chart.axis': 'fgFaint', 'chart.guide': 'border',
    'ports.iconRunningProcessForeground': 'green', 'commentsView.resolvedIcon': 'fgFaint', 'commentsView.unresolvedIcon': 'accent',
    'actionBar.toggledBackground': 'accent@40', 'simpleFindWidget.sashBorder': 'border',
    'gauge.background': 'accent@40', 'gauge.foreground': 'accent', 'gauge.border': N,
    'gauge.warningBackground': 'warm@40', 'gauge.warningForeground': 'warm', 'gauge.errorBackground': 'red@40', 'gauge.errorForeground': 'red',
    'markdownAlert.note.foreground': 'blue', 'markdownAlert.tip.foreground': 'green', 'markdownAlert.important.foreground': 'accent',
    'markdownAlert.warning.foreground': 'warm', 'markdownAlert.caution.foreground': 'red',
    # ---- chat / inline chat / agents
    'chat.requestBorder': 'border', 'chat.requestBackground': 'bgWidget', 'chat.slashCommandBackground': 'accent@26',
    'chat.slashCommandForeground': 'accent', 'chat.avatarBackground': 'badge', 'chat.avatarForeground': 'fg',
    'chat.editedFileForeground': 'blue', 'chat.linesAddedForeground': 'green', 'chat.linesRemovedForeground': 'red',
    'chat.requestCodeBorder': 'border', 'chat.requestBubbleBackground': 'bgWidget', 'chat.requestBubbleHoverBackground': 'bgHover2',
    'chat.checkpointSeparator': 'border', 'chat.thinkingShimmer': 'accent',
    'inlineChat.background': 'bgWidget', 'inlineChat.foreground': 'fg', 'inlineChat.border': 'border', 'inlineChat.shadow': 'black@66',
    'inlineChatInput.border': 'border', 'inlineChatInput.focusBorder': 'accent@80', 'inlineChatInput.placeholderForeground': 'fgFaint',
    'inlineChatInput.background': 'bgDark', 'inlineChatDiff.inserted': 'green@24', 'inlineChatDiff.removed': 'red@24',
    'interactive.activeCodeBorder': 'accent@80', 'interactive.inactiveCodeBorder': 'border',
    'agentsGradient.tintColor': 'accent', 'agentsUpdateButton.downloadingBackground': 'badge', 'agentsUpdateButton.downloadedBackground': 'button',
    'agentsChatInput.focusBorder': 'accent@80', 'agentsChatInput.placeholderForeground': 'fgFaint',
    'agentsNewSessionButton.background': 'button', 'agentsNewSessionButton.foreground': 'white', 'agentsNewSessionButton.border': N,
    'agentsNewSessionButton.hoverBackground': 'buttonHover', 'agentsBadge.background': 'badge', 'agentsBadge.foreground': 'fg',
    'agentsUnreadBadge.background': 'accent', 'agentsUnreadBadge.foreground': 'bgDark',
    'activeSessionView.background': 'bg', 'inactiveSessionView.background': 'bgDark',
    'activeSessionView.foreground': 'fg', 'inactiveSessionView.foreground': 'fgMuted',
    'agentsMobileDiff.addedForeground': 'green', 'agentsMobileDiff.modifiedForeground': 'blue', 'agentsMobileDiff.deletedForeground': 'red',
    'agentSessionReadIndicator.foreground': 'fgFaint', 'agentSessionSelectedBadge.border': 'accent',
    'agentSessionSelectedUnfocusedBadge.border': 'border', 'agentStatusIndicator.background': 'accent',
    'aiCustomizationManagement.sashBorder': 'border', 'chatManagement.sashBorder': 'border',
    # ---- modern UI (preview layout)
    'modernUI.shellBackground': 'bgDark', 'modernUI.inactiveShellBackground': 'bgDark', 'modernSash.gripForeground': 'fgFaint',
    'modernActivityBar.background': 'bgDark', 'modernActivityBar.inactiveBackground': 'bgDark',
    'modernActivityBarItem.activeBackground': 'accent@26', 'modernActivityBarItem.activeForeground': 'fg',
    'modernActivityBarItem.hoverBackground': 'fg@14', 'modernActivityBarItem.hoverForeground': 'fg',
}

SYMBOL = {  # symbol icons -> syntax roles (outline, breadcrumbs, suggest)
    'array': 'syn:prim', 'boolean': 'syn:number', 'class': 'syn:composite', 'color': 'syn:number', 'constant': 'syn:number',
    'constructor': 'syn:method', 'enumerator': 'syn:composite', 'enumeratorMember': 'syn:number', 'event': 'syn:hazard',
    'field': 'syn:member', 'file': 'fgMuted', 'folder': 'fgMuted', 'function': 'syn:function', 'interface': 'syn:composite',
    'key': 'syn:member', 'keyword': 'syn:keyword', 'method': 'syn:method', 'module': 'syn:scope', 'namespace': 'syn:scope',
    'null': 'syn:number', 'number': 'syn:number', 'object': 'syn:prim', 'operator': 'syn:quietop', 'package': 'syn:scope',
    'property': 'syn:member', 'reference': 'cyan', 'snippet': 'syn:directive', 'string': 'syn:string', 'struct': 'syn:composite',
    'text': 'fg', 'typeParameter': 'syn:prim', 'unit': 'syn:unit', 'variable': 'syn:variable',
}
TERMSYM = {
    'alias': 'syn:macro', 'branch': 'accent', 'commit': 'warm', 'flag': 'syn:member', 'option': 'syn:member',
    'optionValue': 'syn:string', 'method': 'syn:function', 'argument': 'syn:param', 'inlineSuggestion': 'fgFaint',
    'file': 'fgMuted', 'folder': 'blue', 'pullRequestDone': 'syn:directive', 'pullRequest': 'green', 'remote': 'cyan',
    'stash': 'syn:number', 'symbolText': 'fg', 'symbolicLinkFile': 'cyan', 'symbolicLinkFolder': 'cyan', 'tag': 'warm',
}

# generic fallbacks for anything not listed (checked in order)
FALLBACK = [
    (r'(^|\.)(shadow)$|Shadow$', 'black@66'),
    (r'(Border|border|Outline|outline)$', 'border'),
    (r'(Background|background)$', 'bgWidget'),
    (r'(Foreground|foreground)$', 'fg'),
]


def assign(key):
    if key in EXPLICIT:
        return EXPLICIT[key]
    m = re.fullmatch(r'symbolIcon\.(\w+)Foreground', key)
    if m and m.group(1) in SYMBOL:
        return SYMBOL[m.group(1)]
    m = re.fullmatch(r'terminalSymbolIcon\.(\w+?)(Foreground)?', key)
    if m and m.group(1) in TERMSYM:
        return TERMSYM[m.group(1)]
    m = re.fullmatch(r'editorIndentGuide\.(background|activeBackground)(\d)', key)
    if m:
        return 'indent' if m.group(1) == 'background' else 'indentActive'
    m = re.fullmatch(r'editorBracketPairGuide\.activeBackground(\d)', key)
    if m:
        return f'br{m.group(1)}@99'
    # modern tabs / editor tabs
    if key.startswith(('modernTab.', 'modernEditorTab.')):
        if 'Foreground' in key:
            return 'fg' if 'active' in key.lower() or 'hover' in key.lower() else 'fgMuted'
        if 'ActionBackground' in key:
            return 'fg@1A'
        if key.endswith('activeBackground') or key.endswith('activeHoverBackground'):
            return 'bg'
        if 'inactive' in key:
            return 'bgDark'
        return 'bgHover'
    if key.startswith(('agents', 'agentFeedback')):
        if key.endswith(('border', 'Border')):
            return 'border'
        if key.endswith(('foreground', 'Foreground')):
            return 'fg'
        return 'bgDark' if key in ('agents.background', 'agentsPanel.background') else 'bgWidget'
    if key in ('modernPanel.border', 'modernActivityBar.border'):
        return 'border'
    for rx, v in FALLBACK:
        if re.search(rx, key):
            return v
    return None
